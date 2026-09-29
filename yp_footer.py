"""Minimal footer."""
from yp_config import EMAIL, FULL_NAME, GITHUB_URL, LINKEDIN_URL, TITLE, YEAR
from yp_helpers import esc, is_set, render


def render_footer() -> None:
    mail = f'<a href="mailto:{esc(EMAIL)}">Email</a>' if is_set(EMAIL) else ""
    render(f"""
    <div class="yp">
      <footer class="footer">
        <div class="wrap footer-in">
          <div><b>{esc(FULL_NAME)}</b><br>{esc(TITLE)}</div>
          <div>© {YEAR} Youssef Abady</div>
          <div class="footer-links">
            <a href="{esc(GITHUB_URL)}" target="_blank" rel="noopener noreferrer">GitHub</a>
            <a href="{esc(LINKEDIN_URL)}" target="_blank" rel="noopener noreferrer">LinkedIn</a>{mail}
          </div>
        </div>
      </footer>
    </div>
    """)
