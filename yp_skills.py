"""Skills grouped by category (no fake percentage bars)."""
from yp_config import SKILLS, USED_IN_PROJECTS
from yp_helpers import esc, render


def render_skills() -> None:
    panels = ""
    for group in SKILLS:
        chips = "".join(
            f'<span class="chip{" used" if item in USED_IN_PROJECTS else ""}">{esc(item)}</span>'
            for item in group["items"])
        panels += f'<div class="panel"><h3>{esc(group["title"])}</h3><div class="chips">{chips}</div></div>'
    render(f"""
    <div class="yp">
      <section class="sec" id="skills">
        <div class="wrap">
          <div class="sec-head reveal">
            <h2 class="sec-title">What I work with.</h2>
            <p class="sec-sub">Grouped by what they're for. No percentage bars, because they don't mean anything.</p>
          </div>
          <p class="legend">Used in a project below</p>
          <div class="skills-grid">{panels}</div>
        </div>
      </section>
    </div>
    """)
