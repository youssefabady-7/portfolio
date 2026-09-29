"""Hero: eyebrow, name, role, CTA buttons, socials and the portrait card."""
from yp_config import DISPLAY_NAME, EMAIL, GITHUB_URL, LINKEDIN_URL, LOCATION, TITLE
from yp_helpers import ICON_GITHUB, ICON_LINKEDIN, ICON_MAIL, esc, img_uri, is_set, render

# (left %, top %, delay s, duration s): a handful of slow, faint particles
PARTICLES = [(8, 22, 0, 9), (18, 68, 2, 11), (31, 12, 4, 10), (44, 82, 1, 12), (56, 30, 3, 9),
             (67, 74, 5, 11), (78, 16, 2, 10), (88, 58, 4, 12), (94, 84, 1, 9), (25, 44, 6, 13)]


def _portrait() -> str:
    src = img_uri("profile.jpg")
    if src:
        inner = f'<img src="{src}" alt="Portrait of {esc(DISPLAY_NAME)}" width="760" height="949" fetchpriority="high">'
    else:  # placeholder until assets/profile.jpg exists
        inner = '<div class="portrait-ph"><b>YA</b>Add your photo at assets/profile.jpg</div>'
    return f"""
    <figure class="portrait rise d3">
      <div class="portrait-frame">{inner}<span class="portrait-tag">{esc(LOCATION)}</span></div>
    </figure>"""


def render_hero() -> None:
    dots = "".join(
        f'<span class="dot" style="left:{x}%;top:{y}%;animation-delay:{d}s;animation-duration:{t}s"></span>'
        for x, y, d, t in PARTICLES)
    socials = (f'<a href="{esc(GITHUB_URL)}" target="_blank" rel="noopener noreferrer" aria-label="GitHub">{ICON_GITHUB}</a>'
               f'<a href="{esc(LINKEDIN_URL)}" target="_blank" rel="noopener noreferrer" aria-label="LinkedIn">{ICON_LINKEDIN}</a>')
    if is_set(EMAIL):
        socials += f'<a href="mailto:{esc(EMAIL)}" aria-label="Email">{ICON_MAIL}</a>'

    chain = "<i>→</i>".join(f"<span>{s}</span>" for s in
                            ["AI", "Machine Learning", "NLP", "Generative AI", "RAG", "Intelligent apps"])

    render(f"""
    <div class="yp">
      <section class="hero" id="top">
        <div class="hero-bg" aria-hidden="true">
          <div class="grid-wrap"><div class="grid-bg"></div></div>
          <span class="glow g1"></span><span class="glow g2"></span>{dots}
        </div>
        <div class="wrap hero-grid">
          <div class="hero-copy">
            <p class="eyebrow rise d1">AI / MACHINE LEARNING • COMPUTER SCIENCE</p>
            <h1 class="hero-title rise d2"><span>Youssef</span><span>Abady</span></h1>
            <p class="hero-role rise d3">{esc(TITLE)}</p>
            <p class="hero-desc rise d4">I build intelligent systems that turn machine learning concepts into practical AI applications.</p>
            <div class="btn-row rise d5">
              <a class="btn btn-primary js-scroll" href="#projects">View My Work</a>
              <a class="btn btn-ghost js-scroll" href="#contact">Let's Connect</a>
            </div>
            <div class="social rise d6">{socials}</div>
            <div class="chain rise d6" aria-label="Focus areas">{chain}</div>
          </div>
          {_portrait()}
        </div>
        <a class="scroll-ind js-scroll" href="#about" aria-label="Scroll to About"><span></span></a>
      </section>
    </div>
    """)
