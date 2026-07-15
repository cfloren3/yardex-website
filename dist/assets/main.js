/* Yardex Guelph — site behaviour (no dependencies) */
(function () {
  "use strict";

  // Header shadow on scroll
  var header = document.querySelector(".site-header");
  var onScroll = function () {
    header.classList.toggle("scrolled", window.scrollY > 8);
  };
  window.addEventListener("scroll", onScroll, { passive: true });
  onScroll();

  // Mobile nav
  var toggle = document.querySelector(".nav-toggle");
  var nav = document.getElementById("site-nav");
  if (toggle && nav) {
    toggle.addEventListener("click", function () {
      var open = nav.classList.toggle("open");
      toggle.setAttribute("aria-expanded", open ? "true" : "false");
    });
    nav.addEventListener("click", function (e) {
      if (e.target.tagName === "A") {
        nav.classList.remove("open");
        toggle.setAttribute("aria-expanded", "false");
      }
    });
  }

  // Scroll reveal (respects reduced motion via CSS)
  if ("IntersectionObserver" in window) {
    var io = new IntersectionObserver(
      function (entries) {
        entries.forEach(function (en) {
          if (en.isIntersecting) {
            en.target.classList.add("in");
            io.unobserve(en.target);
          }
        });
      },
      { threshold: 0.12 }
    );
    document.querySelectorAll(".reveal").forEach(function (el) {
      io.observe(el);
    });
  } else {
    document.querySelectorAll(".reveal").forEach(function (el) {
      el.classList.add("in");
    });
  }

  // Hide sticky CTA while the quote form is on screen
  var sticky = document.querySelector(".sticky-cta");
  var form = document.querySelector('form[name="quote"]');
  if (sticky && form && "IntersectionObserver" in window) {
    new IntersectionObserver(
      function (entries) {
        sticky.classList.toggle("hidden", entries[0].isIntersecting);
      },
      { threshold: 0.05 }
    ).observe(form);
  }

  // Quote form posts natively to FormSubmit; just guard against double-submits
  if (form) {
    form.addEventListener("submit", function () {
      var btn = form.querySelector("button[type='submit']");
      if (btn) {
        btn.textContent = "Sending…";
        setTimeout(function () { btn.disabled = true; }, 0);
      }
    });
  }
})();

/* Review carousel arrows */
(function () {
  document.querySelectorAll(".carousel-wrap").forEach(function (wrap) {
    var track = wrap.querySelector(".carousel");
    var step = function () { return (track.firstElementChild ? track.firstElementChild.offsetWidth + 22 : 340); };
    var prev = wrap.querySelector(".car-btn.prev");
    var next = wrap.querySelector(".car-btn.next");
    if (prev) prev.addEventListener("click", function(){ track.scrollBy({left:-step(), behavior:"smooth"}); });
    if (next) next.addEventListener("click", function(){ track.scrollBy({left: step(), behavior:"smooth"}); });
  });
})();

/* Stat count-up when scrolled into view */
(function () {
  var prefersReduced = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  var stats = document.querySelectorAll(".stat b[data-count]");
  if (!stats.length) return;
  var animate = function (el) {
    var target = parseInt(el.getAttribute("data-count"), 10);
    var start = parseInt(el.getAttribute("data-start") || "0", 10);
    var suffix = el.getAttribute("data-suffix") || "";
    if (prefersReduced) { el.textContent = target + suffix; return; }
    var t0 = null, dur = 1400;
    var tick = function (t) {
      if (!t0) t0 = t;
      var p = Math.min((t - t0) / dur, 1);
      p = 1 - Math.pow(1 - p, 3); /* ease-out */
      el.textContent = Math.round(start + (target - start) * p) + suffix;
      if (p < 1) requestAnimationFrame(tick);
      else el.closest(".stat").classList.add("counted");
    };
    requestAnimationFrame(tick);
  };
  if ("IntersectionObserver" in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting) { animate(en.target); io.unobserve(en.target); }
      });
    }, { threshold: 0.6 });
    stats.forEach(function (el) { io.observe(el); });
  } else {
    stats.forEach(animate);
  }
})();
