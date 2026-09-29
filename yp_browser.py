"""The only JavaScript in the project (~35 lines, all optional).

It runs inside a zero-height Streamlit component and reaches into the parent page to:
  1. set the meta description / Open Graph tags (Streamlit gives no other way),
  2. make nav links scroll smoothly, and
  3. highlight the nav link for the section currently on screen.

If it fails or is blocked, the site still works: plain #anchors + CSS scroll-behavior.
"""
import json

import streamlit.components.v1 as components

from yp_config import DISPLAY_NAME, META_DESCRIPTION, TITLE

_JS = """
<script>
(function () {
  try {
    var d = window.parent.document;
    function meta(key, value, prop) {
      var attr = prop ? 'property' : 'name';
      var m = d.head.querySelector('meta[' + attr + '="' + key + '"]');
      if (!m) { m = d.createElement('meta'); m.setAttribute(attr, key); d.head.appendChild(m); }
      m.setAttribute('content', value);
    }
    meta('description', __DESC__);
    meta('og:title', __TITLE__, true);
    meta('og:description', __DESC__, true);
    meta('theme-color', '#0d0e12');
    d.documentElement.lang = 'en';

    if (!d.__ypBound) {
      d.__ypBound = true;
      var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
      d.addEventListener('click', function (e) {
        var a = e.target.closest && e.target.closest('a.js-scroll');
        if (!a) return;
        var el = d.getElementById(a.getAttribute('href').slice(1));
        if (!el) return;
        e.preventDefault();
        el.scrollIntoView({ behavior: reduce ? 'auto' : 'smooth', block: 'start' });
      });
      var ids = ['top', 'about', 'skills', 'projects', 'education', 'contact'], tries = 0;
      (function spy() {
        var els = ids.map(function (i) { return d.getElementById(i); });
        if (els.some(function (x) { return !x; })) { if (tries++ < 30) setTimeout(spy, 300); return; }
        var io = new IntersectionObserver(function (entries) {
          entries.forEach(function (en) {
            if (!en.isIntersecting) return;
            d.querySelectorAll('.nav-links a').forEach(function (l) {
              l.classList.toggle('active', l.getAttribute('href') === '#' + en.target.id);
            });
          });
        }, { rootMargin: '-45% 0px -50% 0px' });
        els.forEach(function (x) { io.observe(x); });
      })();
    }
  } catch (err) { /* the page works without this script */ }
})();
</script>
"""


def inject() -> None:
    desc = json.dumps(META_DESCRIPTION)
    title = json.dumps(f"{DISPLAY_NAME} | {TITLE}")
    try:
        components.html(_JS.replace("__DESC__", desc).replace("__TITLE__", title), height=0)
    except Exception:  # never let a cosmetic script break the app
        pass
