"""Final call-to-action."""
from yp_config import EMAIL, GITHUB_URL, LINKEDIN_URL, LOCATION
from yp_helpers import ICON_GITHUB, ICON_LINKEDIN, ICON_MAIL, esc, is_set, render


def render_contact() -> None:
    email_btn = (f'<a class="btn btn-primary" href="mailto:{esc(EMAIL)}">{ICON_MAIL}Email Me</a>'
                 if is_set(EMAIL) else "")
    li_cls = "btn-ghost" if is_set(EMAIL) else "btn-primary"
    render(f"""
    <div class="yp">
      <section class="sec contact" id="contact">
        <div class="wrap">
          <h2 class="reveal">Let's build something intelligent.</h2>
          <p class="lead">I'm always interested in learning, building, and collaborating on meaningful AI projects.</p>
          <div class="btn-row">
            {email_btn}
            <a class="btn {li_cls}" href="{esc(LINKEDIN_URL)}" target="_blank" rel="noopener noreferrer">{ICON_LINKEDIN}LinkedIn</a>
            <a class="btn btn-ghost" href="{esc(GITHUB_URL)}" target="_blank" rel="noopener noreferrer">{ICON_GITHUB}GitHub</a>
          </div>
          <p class="loc">{esc(LOCATION)}</p>
        </div>
      </section>
    </div>
    """)
