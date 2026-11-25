/* Yardex conversion events (r1).
   Sends lead actions to whichever analytics tool is installed: GA4 (gtag),
   Google Tag Manager (dataLayer) or Vercel Web Analytics (va). With none of
   them on the page it does nothing. It collects no personal data: only the
   action type, the page path and the link's destination path. */
(function () {
  "use strict";
  function send(name, params) {
    params = params || {};
    params.page_path = location.pathname;
    try {
      if (typeof window.gtag === "function") window.gtag("event", name, params);
      else if (Array.isArray(window.dataLayer)) window.dataLayer.push(Object.assign({ event: name }, params));
      if (typeof window.va === "function") window.va("event", { name: name, data: params });
    } catch (e) { /* never break the page for analytics */ }
  }
  document.addEventListener("click", function (e) {
    var a = e.target.closest && e.target.closest("a[href]");
    if (!a) return;
    var href = a.getAttribute("href") || "";
    var where = a.closest("header") ? "header" : a.closest("footer") ? "footer" :
                a.closest(".sticky-cta") ? "sticky_bar" : a.closest(".hero, .hero--sub") ? "hero" : "content";
    if (href.indexOf("tel:") === 0) send("phone_click", { link_location: where });
    else if (href.indexOf("sms:") === 0) send("text_click", { link_location: where });
    else if (href.indexOf("mailto:") === 0) send("email_click", { link_location: where });
    else if (/^\/quote\/?(#.*)?$/.test(href)) send("quote_button_click", { link_location: where });
  }, { passive: true });
  // Quote form: one event per submission attempt (the form posts to FormSubmit,
  // which then redirects to /thank-you/, where the confirmed lead is counted).
  document.addEventListener("submit", function (e) {
    var f = e.target;
    if (!f || f.dataset.ydxTracked) return;
    if (/formsubmit\.co/.test(f.getAttribute("action") || "")) { f.dataset.ydxTracked = "1"; send("quote_form_submit"); }
  });
  if (/^\/thank-you\/?$/.test(location.pathname)) {
    try {
      if (!sessionStorage.getItem("ydx_lead")) { sessionStorage.setItem("ydx_lead", "1"); send("generate_lead", { method: "quote_form" }); }
    } catch (e) { send("generate_lead", { method: "quote_form" }); }
  }
})();
