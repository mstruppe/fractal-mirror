/* FRACTAL site — shared behaviors (unified at the structure pass, 2026-08-17).
   Floats, copy buttons, subnav scrollspy, and the attention-follow subnav:
   it slides down out of the top when the cursor moves, and back up when it rests. */
(function () {
  var reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  /* reveal-on-scroll */
  var floats = document.querySelectorAll(".float");
  if (reduce || !("IntersectionObserver" in window)) {
    floats.forEach(function (el) { el.classList.add("in"); });
  } else {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting) { e.target.classList.add("in"); io.unobserve(e.target); }
      });
    }, { threshold: 0.12 });
    floats.forEach(function (el) { io.observe(el); });
  }

  /* copy buttons (clipboard API needs a secure context; fall back to a hidden textarea) */
  document.querySelectorAll(".copy").forEach(function (btn) {
    btn.addEventListener("click", function () {
      var text = btn.parentElement.textContent.replace(/copy$/, "").trim();
      function done() {
        btn.textContent = "copied";
        setTimeout(function () { btn.textContent = "copy"; }, 1600);
      }
      if (navigator.clipboard && navigator.clipboard.writeText) {
        navigator.clipboard.writeText(text).then(done, function () { fallback(); });
      } else { fallback(); }
      function fallback() {
        var ta = document.createElement("textarea");
        ta.value = text;
        ta.style.position = "fixed"; ta.style.opacity = "0";
        document.body.appendChild(ta);
        ta.select();
        try { document.execCommand("copy"); done(); } catch (e) {}
        document.body.removeChild(ta);
      }
    });
  });

  /* subnav */
  var subnav = document.querySelector("nav.subnav");
  if (!subnav) return;

  /* scrollspy */
  var links = Array.prototype.slice.call(subnav.querySelectorAll("a[href^='#']"));
  if (links.length && "IntersectionObserver" in window) {
    var spy = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (!e.isIntersecting) return;
        links.forEach(function (l) { l.classList.toggle("active", l.getAttribute("href") === "#" + e.target.id); });
      });
    }, { rootMargin: "-40% 0px -55% 0px" });
    links.forEach(function (l) {
      var t = document.getElementById(l.getAttribute("href").slice(1));
      if (t) spy.observe(t);
    });
  }

  /* attention-follow: show on cursor/scroll/touch/key activity, collapse at rest.
     On the home page the hero additionally gates it (hidden until scrolled past). */
  subnav.classList.remove("reveal", "show");
  subnav.classList.add("auto");
  var hero = document.querySelector("header.hero");
  /* without IntersectionObserver the hero gate can never open — so it doesn't gate */
  var pastHero = !hero || !("IntersectionObserver" in window);
  var active = true;
  var timer = null;
  var REST_MS = 1800;

  function update() {
    subnav.classList.toggle("shown", pastHero && active);
  }
  function rest() {
    /* never collapse while the cursor or keyboard focus is on the menus */
    if (subnav.matches(":hover") || subnav.contains(document.activeElement)) { poke(); return; }
    var top = document.querySelector("nav.top");
    if (top && top.matches(":hover")) { poke(); return; }
    active = false; update();
  }
  function poke() {
    active = true; update();
    if (timer) clearTimeout(timer);
    timer = setTimeout(rest, REST_MS);
  }
  if (hero && "IntersectionObserver" in window) {
    new IntersectionObserver(function (entries) {
      pastHero = !entries[0].isIntersecting;
      update();
    }, { threshold: 0.25 }).observe(hero);
  }
  ["mousemove", "wheel", "scroll", "touchstart", "keydown"].forEach(function (ev) {
    window.addEventListener(ev, poke, { passive: true });
  });
  poke();
})();
