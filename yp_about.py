"""About: short human copy + the learn / build / experiment / improve loop."""
from yp_helpers import render

INTERESTS = ["Machine Learning", "NLP", "Generative AI", "RAG systems", "AI applications",
             "Intelligent agents", "Data processing"]

LOOP = [
    ("LEARN", "Take a concept from a course, a paper, or a lecture."),
    ("BUILD", "Turn it into code that actually runs."),
    ("EXPERIMENT", "Change things, break things, compare results."),
    ("IMPROVE", "Fix what broke, then make it cleaner."),
]


def render_about() -> None:
    chips = "".join(f'<span class="chip">{i}</span>' for i in INTERESTS)
    steps = "".join(
        f'<li class="loop-step"><div><div class="loop-word">{w}</div><div class="loop-desc">{d}</div></div></li>'
        for w, d in LOOP)
    render(f"""
    <div class="yp">
      <section class="sec" id="about">
        <div class="wrap">
          <div class="sec-head reveal"><h2 class="sec-title">Building, not just studying.</h2></div>
          <div class="about-grid">
            <div class="about-copy">
              <p>I'm a Computer Science student at Alexandria University, building my AI/ML engineering foundation through hands-on projects.</p>
              <p>I learn by building. When a concept clicks in class, like embeddings, retrieval, or automata, I try to put it into something that runs.</p>
              <p>I'm early in the journey, and I'd rather show working projects than long lists of buzzwords.</p>
              <div class="chips" aria-label="Interests">{chips}</div>
            </div>
            <div class="loop" role="group" aria-label="How I learn">
              <ol style="display:contents">{steps}</ol>
              <div class="loop-return">then back to LEARN</div>
            </div>
          </div>
        </div>
      </section>
    </div>
    """)
