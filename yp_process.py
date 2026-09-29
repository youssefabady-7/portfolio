"""How I Build (4 stages) + Currently Exploring."""
from yp_config import EXPLORING
from yp_helpers import esc, render

STEPS = [
    ("01", "Understand", "Define the problem and the requirements before writing code."),
    ("02", "Design", "Think through the architecture, the data flow, and the components."),
    ("03", "Build", "Implement the system and wire the AI parts into it."),
    ("04", "Improve", "Test, debug, evaluate, and iterate."),
]


def render_process() -> None:
    steps = "".join(
        f'<li class="step"><span class="step-n">{n}</span><h3>{t}</h3><p>{d}</p></li>' for n, t, d in STEPS)
    render(f"""
    <div class="yp">
      <section class="sec" id="process" style="padding-top:0;padding-bottom:clamp(24px,4vw,56px)">
        <div class="wrap">
          <div class="sec-head reveal">
            <h2 class="sec-title">How I build.</h2>
            <p class="sec-sub">Calling a model API is the easy part. The engineering is everything around it.</p>
          </div>
          <ol class="steps">{steps}</ol>
        </div>
      </section>
    </div>
    """)


def render_exploring() -> None:
    chips = "".join(f'<span class="chip big">{esc(t)}</span>' for t in EXPLORING)
    render(f"""
    <div class="yp">
      <section class="explore" id="exploring">
        <div class="wrap">
          <h2>Currently exploring</h2>
          <p>Not a list of things I've mastered. It's what I'm working through right now.</p>
          <div class="chips">{chips}</div>
        </div>
      </section>
    </div>
    """)
