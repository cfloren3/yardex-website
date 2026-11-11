/* The Yardex Difference: scroll-controlled image-sequence player (no dependencies).
   - Static mode stays in place unless the inline script added .ydx--live
     (no reduced-motion, no Save-Data, IntersectionObserver available).
   - Frames load only when the section gets close, coarse-to-fine, so scrubbing
     works early and sharpens as the rest arrive. */
(function () {
  "use strict";
  var root = document.querySelector("[data-ydx]");
  if (!root || !root.classList.contains("ydx--live")) return;

  var track = root.querySelector(".ydx__track");
  var canvas = root.querySelector(".ydx__canvas");
  var ctx = canvas.getContext("2d", { alpha: false });
  var steps = [].slice.call(root.querySelectorAll(".ydx__step"));
  var bars = [].slice.call(root.querySelectorAll(".ydx__rail i"));
  var end = root.querySelector(".ydx__end");
  var base = root.getAttribute("data-base");
  var bounds = root.getAttribute("data-stages").split(",").map(Number);
  var TOTAL = bounds[bounds.length - 1];

  var mobile = window.matchMedia("(max-width: 767px)").matches && window.innerHeight > window.innerWidth;
  var set = mobile ? "m" : "d";
  var count = +root.getAttribute("data-count-" + set);
  var frames = new Array(count), started = false, inView = false;
  var cur = 0, target = 0, drawn = -1, raf = 0;

  // Scroll phases (fractions of the track): intro, footage, end card.
  var V0 = 0.035, V1 = 0.9, E0 = 0.9, E1 = 0.96;
  var clamp = function (v, a, b) { return v < a ? a : v > b ? b : v; };
  var smooth = function (k) { k = clamp(k, 0, 1); return k * k * (3 - 2 * k); };

  function src(i) { return base + set + "/" + ("000" + i).slice(-4) + ".webp"; }

  // coarse-to-fine order: 0, then every 32nd, 16th, 8th, 4th, 2nd, all
  function order() {
    var seen = {}, out = [];
    [count, 32, 16, 8, 4, 2, 1].forEach(function (s) {
      for (var i = 0; i < count; i += s) if (!seen[i]) { seen[i] = 1; out.push(i); }
    });
    if (!seen[count - 1]) out.push(count - 1);
    return out;
  }

  function load() {
    if (started) return;
    started = true;
    var queue = order(), active = 0, MAX = 6;
    function next() {
      while (active < MAX && queue.length) {
        (function (i) {
          var img = new Image();
          img.decoding = "async";
          active++;
          img.onload = function () {
            frames[i] = img; active--;
            if (i === 0) root.classList.add("ydx--ready");
            drawn = -1; tick(); next();
          };
          img.onerror = function () { active--; next(); };
          img.src = src(i);
        })(queue.shift());
      }
    }
    next();
  }

  function nearest(i) {
    if (frames[i]) return frames[i];
    for (var d = 1; d < count; d++) {
      if (frames[i - d]) return frames[i - d];
      if (frames[i + d]) return frames[i + d];
    }
    return null;
  }

  function size() {
    var dpr = Math.min(window.devicePixelRatio || 1, 2);
    var w = Math.round(canvas.clientWidth * dpr), h = Math.round(canvas.clientHeight * dpr);
    if (canvas.width !== w || canvas.height !== h) { canvas.width = w; canvas.height = h; drawn = -1; }
  }

  function draw(i) {
    var img = nearest(i);
    if (!img) return;
    var cw = canvas.width, ch = canvas.height, iw = img.naturalWidth, ih = img.naturalHeight;
    var s = Math.max(cw / iw, ch / ih), w = iw * s, h = ih * s;
    ctx.drawImage(img, (cw - w) / 2, (ch - h) / 2, w, h);
    drawn = img === frames[i] ? i : -1;
  }

  function progress() {
    var r = track.getBoundingClientRect(), span = r.height - window.innerHeight;
    return span > 0 ? clamp(-r.top / span, 0, 1) : 0;
  }

  function ui(p, t) {
    root.style.setProperty("--ydx-intro", (1 - smooth((p - 0.004) / (V0 + 0.02))).toFixed(3));
    var e = smooth((p - E0) / (E1 - E0));
    root.style.setProperty("--ydx-end", e.toFixed(3));
    end.classList.toggle("is-on", e > 0.01);
    var stage = 0;
    for (var s = 0; s < bounds.length - 1; s++) {
      var f = clamp((t - bounds[s]) / (bounds[s + 1] - bounds[s]), 0, 1);
      if (bars[s]) bars[s].style.setProperty("--f", f.toFixed(3));
      if (t >= bounds[s]) stage = s;
    }
    var showCaption = p > V0 && e < 0.4;
    steps.forEach(function (el, i) { el.classList.toggle("is-on", showCaption && i === stage); });
  }

  function tick() {
    if (raf) return;
    raf = requestAnimationFrame(function loop() {
      raf = 0;
      var p = progress(), v = clamp((p - V0) / (V1 - V0), 0, 1);
      target = v * (count - 1);
      cur += (target - cur) * 0.25;
      if (Math.abs(target - cur) < 0.05) cur = target;
      var i = Math.round(cur);
      if (i !== drawn) draw(i);
      ui(p, (cur / (count - 1)) * TOTAL);
      if (inView && cur !== target) raf = requestAnimationFrame(loop);
    });
  }

  // start loading half a screen before the section arrives, and never before the page
  // itself has finished loading (keeps the page's own images and LCP fast)
  function whenLoaded(fn) { if (document.readyState === "complete") fn(); else window.addEventListener("load", fn, { once: true }); }
  whenLoaded(function () {
    new IntersectionObserver(function (en) { if (en[0].isIntersecting) { load(); size(); tick(); } }, { rootMargin: "50% 0px" }).observe(root);
  });
  new IntersectionObserver(function (en) { inView = en[0].isIntersecting; if (inView) tick(); }).observe(root);
  window.addEventListener("scroll", function () { if (inView) tick(); }, { passive: true });
  window.addEventListener("resize", function () { size(); tick(); });
})();
