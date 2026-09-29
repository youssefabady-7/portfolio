"""Sticky top navigation (plain HTML, smooth-scroll handled by CSS + a tiny JS helper)."""
from yp_config import DISPLAY_NAME
from yp_helpers import esc, render

LINKS = [("about", "About"), ("skills", "Skills"), ("projects", "Projects"),
         ("education", "Education"), ("contact", "Contact")]


def render_nav() -> None:
    links = "".join(f'<a class="js-scroll" href="#{i}">{label}</a>' for i, label in LINKS)
    render(f"""
    <div class="yp">
      <nav class="nav" aria-label="Primary">
        <div class="nav-in">
          <a class="brand js-scroll" href="#top" aria-label="{esc(DISPLAY_NAME)} — back to top">
            <span class="full">{esc(DISPLAY_NAME)}</span><span class="short">YA</span>
          </a>
          <div class="nav-links">{links}</div>
        </div>
      </nav>
    </div>
    """)
