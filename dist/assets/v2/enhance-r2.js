/* Yardex Guelph 2.0 — enhancement layer (runs after the original main.js).
   Adds motion and interaction only; all content is already in the HTML.
   No dependencies. Respects prefers-reduced-motion. */
(function () {
  "use strict";
  var reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  var finePointer = window.matchMedia("(hover: hover) and (pointer: fine)").matches;
  var wide = window.matchMedia("(min-width: 1000px)").matches;
  var hasIO = "IntersectionObserver" in window;

  var onEnter = function (els, cb, opts) {
    if (!els.length) return;
    if (!hasIO || reduce) { els.forEach(cb); return; }
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) { if (en.isIntersecting) { cb(en.target); io.unobserve(en.target); } });
    }, opts || { threshold: 0.18, rootMargin: "0px 0px -8% 0px" });
    els.forEach(function (el) { io.observe(el); });
  };
  var $$ = function (sel, root) { return Array.prototype.slice.call((root || document).querySelectorAll(sel)); };

  /* 0. Load the enhancement stylesheet now (kept off the critical path so the
        original page paints first; a <noscript> fallback exists in the HTML). */
  if (!document.querySelector('link[href="/assets/v2/enhance-r2.css"]')) {
    var css = document.createElement("link");
    css.rel = "stylesheet"; css.href = "/assets/v2/enhance-r2.css";
    document.head.appendChild(css);
  }

  /* 1. Scroll progress hairline */
  var bar = document.createElement("div");
  bar.className = "scroll-progress"; bar.setAttribute("aria-hidden", "true");
  document.body.appendChild(bar);
  if (!CSS.supports || !CSS.supports("animation-timeline: scroll()")) {
    var setBar = function () {
      var h = document.documentElement.scrollHeight - window.innerHeight;
      bar.style.transform = "scaleX(" + (h > 0 ? Math.min(window.scrollY / h, 1) : 0) + ")";
    };
    window.addEventListener("scroll", setBar, { passive: true }); setBar();
  }

  /* 2. Header tucks away when scrolling down, returns when scrolling up */
  var header = document.querySelector(".site-header");
  var lastY = window.scrollY, ticking = false;
  if (header && !reduce) {
    window.addEventListener("scroll", function () {
      if (ticking) return; ticking = true;
      requestAnimationFrame(function () {
        var y = window.scrollY, nav = document.getElementById("site-nav");
        var open = nav && nav.classList.contains("open");
        if (!open && y > 420 && y > lastY + 6) header.classList.add("tucked");
        else if (y < lastY - 6 || y < 420) header.classList.remove("tucked");
        lastY = y; ticking = false;
      });
    }, { passive: true });
    header.addEventListener("focusin", function () { header.classList.remove("tucked"); });
  }

  /* 3. Stagger sibling reveals inside grids (the original main.js adds .in) */
  $$(".svc-grid, .award-row, .grid-3, .grid-4, .stats .container, .creds, .badge-wall, .blog-list, .carousel, .ba-grid, .photo-trio, .motion-grid").forEach(function (grid) {
    $$(":scope > .reveal", grid).forEach(function (el, i) {
      if (!el.style.transitionDelay) el.style.transitionDelay = (Math.min(i, 6) * 0.08) + "s";
    });
  });

  /* 4. Word-by-word reveal for section headings (H2 only; text stays in the DOM) */
  if (!reduce) {
    var heads = $$("main h2").filter(function (h) {
      return !h.closest(".hero") && h.children.length === 0 && h.textContent.trim().split(/\s+/).length <= 12;
    });
    heads.forEach(function (h) {
      var words = h.textContent.trim().split(/\s+/);
      h.setAttribute("aria-label", h.textContent.trim());
      h.textContent = "";
      words.forEach(function (w, i) {
        var outer = document.createElement("span"); outer.className = "split-word"; outer.setAttribute("aria-hidden", "true");
        var inner = document.createElement("span"); inner.textContent = w; inner.style.setProperty("--i", i);
        outer.appendChild(inner); h.appendChild(outer);
        if (i < words.length - 1) h.appendChild(document.createTextNode(" "));
      });
    });
    onEnter(heads, function (h) { h.classList.add("split-in"); }, { threshold: 0.3 });
  }

  /* 5. Generic "in" for new components (timeline, marks, chips, standalone images) */
  onEnter($$(".timeline, .marks, .img-reveal"), function (el) { el.classList.add("in"); });
  $$(".area-chips li").forEach(function (li, i) { li.style.setProperty("--i", i); });

  /* 6. Counters with decimals / suffix (new elements only; originals stay on main.js) */
  var countUp = function (el) {
    var target = parseFloat(el.getAttribute("data-countup"));
    var dec = parseInt(el.getAttribute("data-decimals") || "0", 10);
    var suffix = el.getAttribute("data-suffix") || "";
    var fill = el.closest("[data-rating]");
    if (fill) fill.style.setProperty("--fill", "100%");
    if (reduce) { el.textContent = target.toFixed(dec) + suffix; return; }
    var t0 = null, dur = 1600;
    var tick = function (t) {
      if (!t0) t0 = t;
      var p = Math.min((t - t0) / dur, 1); p = 1 - Math.pow(1 - p, 4);
      el.textContent = (target * p).toFixed(dec) + suffix;
      if (p < 1) requestAnimationFrame(tick);
    };
    requestAnimationFrame(tick);
  };
  $$("[data-rating]").forEach(function (r) { if (!reduce) r.style.setProperty("--fill", "0%"); });
  onEnter($$("[data-countup]"), countUp, { threshold: 0.6 });

  /* 7. Subtle parallax for existing photo-backed sections (desktop only) */
  var px = $$(".identity, .section--photo-light, .hero--sub, .photo-band");
  if (px.length && !reduce && wide) {
    var pTick = false;
    var update = function () {
      var vh = window.innerHeight;
      px.forEach(function (s) {
        var r = s.getBoundingClientRect();
        if (r.bottom < -100 || r.top > vh + 100) return;
        var p = (r.top + r.height / 2 - vh / 2) / (vh + r.height);
        s.style.setProperty("--py", (p * -70).toFixed(1) + "px");
      });
      pTick = false;
    };
    window.addEventListener("scroll", function () { if (!pTick) { pTick = true; requestAnimationFrame(update); } }, { passive: true });
    window.addEventListener("resize", update); update();
  }

  /* 8. Gentle 3D tilt on cards (mouse/trackpad only) */
  if (finePointer && !reduce) {
    $$(".award-card, .mark").forEach(function (card) {
      card.classList.add("tilt");
      card.addEventListener("pointermove", function (e) {
        var r = card.getBoundingClientRect();
        var x = (e.clientX - r.left) / r.width - 0.5, y = (e.clientY - r.top) / r.height - 0.5;
        card.style.setProperty("--ry", (x * 4).toFixed(2) + "deg");
        card.style.setProperty("--rx", (y * -4).toFixed(2) + "deg");
      });
      card.addEventListener("pointerleave", function () { card.style.setProperty("--rx", "0deg"); card.style.setProperty("--ry", "0deg"); });
    });
  }

  /* 9. Drag-to-scroll for the review and process carousels (desktop) */
  if (finePointer) {
    $$(".carousel").forEach(function (c) {
      var down = false, sx = 0, sl = 0, moved = false;
      c.addEventListener("pointerdown", function (e) { if (e.pointerType !== "mouse") return; down = true; moved = false; sx = e.clientX; sl = c.scrollLeft; });
      window.addEventListener("pointermove", function (e) {
        if (!down) return; var dx = e.clientX - sx;
        if (Math.abs(dx) > 4) { moved = true; c.classList.add("dragging"); }
        c.scrollLeft = sl - dx;
      });
      window.addEventListener("pointerup", function () {
        if (!down) return; down = false;
        if (moved) { c.classList.remove("dragging"); var w = c.firstElementChild ? c.firstElementChild.offsetWidth + 22 : 1; c.scrollTo({ left: Math.round(c.scrollLeft / w) * w, behavior: "smooth" }); }
      });
    });
  }

  /* 10. Lightbox for the photo gallery (images only; nothing navigates away) */
  var gal = $$(".gallery-track img, .zoomable img");
  if (gal.length && typeof HTMLDialogElement === "function") {
    var seen = {}, list = gal.filter(function (im) { if (seen[im.src]) return false; seen[im.src] = 1; return true; });
    var dlg = document.createElement("dialog");
    dlg.className = "lightbox"; dlg.setAttribute("aria-label", "Photo viewer");
    dlg.innerHTML = '<img alt=""><p></p><button class="lb-btn lb-prev" aria-label="Previous photo">‹</button><button class="lb-btn lb-next" aria-label="Next photo">›</button><button class="lb-close" aria-label="Close photo viewer">✕</button>';
    document.body.appendChild(dlg);
    var big = dlg.querySelector("img"), cap = dlg.querySelector("p"), idx = 0;
    var show = function (i) { idx = (i + list.length) % list.length; big.src = list[idx].currentSrc || list[idx].src; big.alt = list[idx].alt; cap.textContent = list[idx].alt; };
    gal.forEach(function (im) {
      im.setAttribute("tabindex", "0"); im.setAttribute("role", "button");
      var open = function () { show(list.indexOf(list.filter(function (x) { return x.src === im.src; })[0])); dlg.showModal(); };
      im.addEventListener("click", open);
      im.addEventListener("keydown", function (e) { if (e.key === "Enter" || e.key === " ") { e.preventDefault(); open(); } });
    });
    dlg.querySelector(".lb-prev").addEventListener("click", function () { show(idx - 1); });
    dlg.querySelector(".lb-next").addEventListener("click", function () { show(idx + 1); });
    dlg.querySelector(".lb-close").addEventListener("click", function () { dlg.close(); });
    dlg.addEventListener("click", function (e) { if (e.target === dlg) dlg.close(); });
    dlg.addEventListener("keydown", function (e) { if (e.key === "ArrowLeft") show(idx - 1); if (e.key === "ArrowRight") show(idx + 1); });
  }

  /* 11. Keep the mobile menu and header in sync */
  var toggle = document.querySelector(".nav-toggle"), nav = document.getElementById("site-nav");
  if (toggle && nav) toggle.addEventListener("click", function () { document.body.classList.toggle("nav-open", nav.classList.contains("open")); });
  /* 11b. Deferred media: band backgrounds and video posters load only when near the viewport */
  var lazyMedia = $$("[data-bg], video[data-poster]");
  var loadMedia = function (el) {
    if (el.hasAttribute("data-bg")) el.style.setProperty("--pb-img", "url('" + el.getAttribute("data-bg") + "')");
    if (el.hasAttribute("data-poster")) el.setAttribute("poster", el.getAttribute("data-poster"));
  };
  if (hasIO) {
    var mio = new IntersectionObserver(function (en) {
      en.forEach(function (e) { if (e.isIntersecting) { loadMedia(e.target); mio.unobserve(e.target); } });
    }, { rootMargin: "600px 0px" });
    lazyMedia.forEach(function (el) { mio.observe(el); });
  } else { lazyMedia.forEach(loadMedia); }

  /* 12. Short lawn clips: play only while on screen; never autoplay for reduced motion */
  $$("video[data-autoplay]").forEach(function (v) {
    v.muted = true;
    if (reduce || !hasIO) { v.setAttribute("controls", ""); return; }
    new IntersectionObserver(function (en) {
      en.forEach(function (e) {
        if (e.isIntersecting) { var p = v.play(); if (p && p.catch) p.catch(function () {}); }
        else v.pause();
      });
    }, { threshold: 0.35 }).observe(v);
  });

  /* 13. Contact button: always one tap from the quote form; steps aside when the form is visible */
  var fab = document.querySelector(".fab-contact");
  var qform = document.getElementById("quote-form");
  if (fab) {
    var formVisible = false, phone = window.matchMedia("(max-width: 760px)");
    var syncFab = function () {
      /* on phones the button waits until the visitor scrolls past the opening screen,
         so it never covers the hero text; on desktop it is always available */
      var early = phone.matches && window.scrollY < window.innerHeight * 0.6;
      fab.classList.toggle("fab-hidden", formVisible || early);
    };
    if (qform && hasIO) {
      new IntersectionObserver(function (en) { formVisible = en[0].isIntersecting; syncFab(); }, { threshold: 0.05 }).observe(qform);
    }
    window.addEventListener("scroll", syncFab, { passive: true });
    window.addEventListener("resize", syncFab);
    syncFab();
  }
})();
