"""Projects: Study Buddy (featured, with RAG architecture) + a grid of other work."""
from yp_config import (DATA_STRUCTURES_REPO_URL, GITHUB_URL, STUDY_BUDDY_DEMO_URL, STUDY_BUDDY_GITHUB_URL,
                    STUDY_BUDDY_MY_ROLE, STUDY_BUDDY_TEAM, TOC_REPO_URL)
from yp_helpers import ICON_GITHUB, esc, img_uri, is_set, render

# ------------------------------------------------------------------ Study Buddy content
FEATURES = [
    ("AI-powered document chat", "Ask questions about your own PDFs."),
    ("RAG-based answers", "Grounded in retrieved passages. If the material doesn't cover it, it says so."),
    ("Flashcard generation", "Generate a deck and flip through it card by card."),
    ("Quiz generation", "Multiple choice at three difficulty levels, scored at the end."),
    ("Text-to-speech", "Chat answers can be read aloud with Kokoro."),
    ("PDF processing", "Extracts and chunks course material so it can be searched."),
]

INDEX_LANE = [
    ("PDF", "Your course material", False),
    ("Text extraction", "pypdf", False),
    ("Text chunking", "Split into passages", False),
    ("Embeddings", "all-MiniLM-L6-v2", True),
]
ANSWER_LANE = [
    ("Vector search", "FAISS index", True),
    ("Relevant context", "Best-matching passages", False),
    ("LLM", "Groq · gpt-oss-120b", False),
    ("Grounded answer", "Text, optionally spoken", False),
]

TECH = ["Python", "Streamlit", "RAG", "Embeddings", "Vector Search", "FAISS", "LLM", "NLP", "TTS", "PDF Processing"]


def _btn(url: str, label: str, primary: bool, icon: str = "") -> str:
    cls = "btn-primary" if primary else "btn-ghost"
    if not is_set(url):
        return f'<span class="btn btn-off" aria-disabled="true">{label} (link coming soon)</span>'
    return (f'<a class="btn {cls}" href="{esc(url)}" target="_blank" rel="noopener noreferrer">'
            f'{icon}{label}</a>')


def _flow(nodes: list[tuple[str, str, bool]]) -> str:
    return "".join(
        f'<div class="node{" key" if key else ""}"><b>{esc(name)}</b><small>{esc(sub)}</small></div>'
        for name, sub, key in nodes)


def _preview() -> str:
    shot = img_uri("study-buddy.png")
    if shot:
        return f'<div class="preview"><img src="{shot}" alt="Screenshot of the Study Buddy app"></div>'
    # Schematic stand-in until a real screenshot is added at assets/study-buddy.png
    return """
    <div class="preview" role="img" aria-label="Schematic of the Study Buddy interface with Chat, Flashcards and Quiz tabs">
      <div class="pv-bar"><i></i><i></i><i></i></div>
      <div class="pv-tabs"><span class="on">Chat</span><span>Flashcards</span><span>Quiz</span></div>
      <div class="pv-body">
        <div class="pv-line a"></div><div class="pv-line c"></div><div class="pv-line b"></div>
        <div class="pv-line d"></div><div class="pv-input"></div>
      </div>
    </div>"""


def _study_buddy() -> str:
    features = "".join(f"<li><strong>{esc(t)}</strong><span>{esc(d)}</span></li>" for t, d in FEATURES)
    tech = "".join(f'<span class="chip tech">{esc(t)}</span>' for t in TECH)
    team = ", ".join(STUDY_BUDDY_TEAM)
    meta = f"Team project · built with {esc(team)}" if STUDY_BUDDY_TEAM else "Team project"
    role = (f'<div class="myrole"><b>My part</b>{esc(STUDY_BUDDY_MY_ROLE)}</div>'
            if is_set(STUDY_BUDDY_MY_ROLE) else "")
    return f"""
    <article class="feature" aria-labelledby="sb-title">
      <p class="eyebrow">FEATURED PROJECT • HCIA-AI V4.0</p>
      <h3 class="feature-title" id="sb-title">Study Buddy</h3>
      <p class="feature-sub">An AI-powered study companion that turns static PDFs into interactive learning experiences.</p>
      <div class="btn-row">
        {_btn(STUDY_BUDDY_DEMO_URL, "Live Demo", True)}
        {_btn(STUDY_BUDDY_GITHUB_URL, "View on GitHub", False, ICON_GITHUB.replace('width="20" height="20"', 'width="18" height="18"'))}
      </div>
      <p class="feature-meta">{meta}</p>

      <div class="feature-cols">
        <div class="story">
          <h4>The problem</h4>
          <p>Students study from long PDFs and lecture notes that are hard to search, hard to understand, and hard to practice from.</p>
          <h4>The solution</h4>
          <p>Study Buddy turns educational PDFs into an interactive AI learning environment: chat with the material, then test yourself on it.</p>
          <ul class="features">{features}</ul>
          {role}
        </div>
        {_preview()}
      </div>

      <div class="rag">
        <h4 class="rag-title">Retrieval-Augmented Generation (RAG)</h4>
        <p class="rag-note">The system retrieves relevant information from the user's uploaded material before generating an answer, helping keep responses grounded in the source content.</p>
        <div class="lane">
          <p class="lane-label">1 · Index the material</p>
          <p class="lane-cap">Once, when you build Study Buddy from a PDF. The embedded chunks are stored in a FAISS index.</p>
          <div class="flow">{_flow(INDEX_LANE)}</div>
        </div>
        <div class="lane">
          <p class="lane-label">2 · Answer a question</p>
          <p class="lane-cap">Every time you ask. The model only sees what retrieval hands it.</p>
          <div class="flow">{_flow(ANSWER_LANE)}</div>
        </div>
      </div>

      <div class="chips" style="margin-top:28px" aria-label="Study Buddy tech stack">{tech}</div>
    </article>
    """


# ------------------------------------------------------------------ small SVG covers
def _svg_automata() -> str:
    return """
    <svg viewBox="0 0 320 180" role="img" aria-label="State diagram of a small finite automaton" preserveAspectRatio="xMidYMid slice">
      <rect width="320" height="180" fill="#111319"/>
      <g fill="none" stroke="#7c8cff" stroke-width="1.6" stroke-linecap="round">
        <circle cx="64" cy="98" r="24" stroke-opacity=".9"/>
        <circle cx="160" cy="98" r="24" stroke-opacity=".9"/>
        <circle cx="256" cy="98" r="24" stroke-opacity=".9"/><circle cx="256" cy="98" r="19" stroke-opacity=".5"/>
        <path d="M18 98h22" /><path d="m34 92 6 6-6 6"/>
        <path d="M88 98h48"/><path d="m130 92 6 6-6 6"/>
        <path d="M184 98h48"/><path d="m226 92 6 6-6 6"/>
        <path d="M148 75c-10-34 34-34 24 0" stroke-opacity=".7"/><path d="m168 70 4 6-7 1" stroke-opacity=".7"/>
        <path d="M244 122c-22 34-158 34-180 0" stroke-opacity=".45" stroke-dasharray="3 5"/>
      </g>
      <g fill="#9298a6" font-family="ui-monospace,Menlo,monospace" font-size="12" text-anchor="middle">
        <text x="64" y="102">q0</text><text x="160" y="102">q1</text><text x="256" y="102">q2</text>
        <text x="112" y="88">a</text><text x="208" y="88">b</text><text x="160" y="44">a</text>
      </g>
    </svg>"""


def _svg_structures() -> str:
    return """
    <svg viewBox="0 0 320 180" role="img" aria-label="A binary tree and a linked list" preserveAspectRatio="xMidYMid slice">
      <rect width="320" height="180" fill="#111319"/>
      <g stroke="#7c8cff" stroke-opacity=".55" stroke-width="1.4" fill="none">
        <path d="M160 48 112 88M160 48 208 88M112 88 84 128M112 88 140 128M208 88 236 128"/>
      </g>
      <g fill="#151820" stroke="#7c8cff" stroke-width="1.6">
        <circle cx="160" cy="40" r="15"/><circle cx="112" cy="88" r="14"/><circle cx="208" cy="88" r="14"/>
        <circle cx="84" cy="130" r="13"/><circle cx="140" cy="130" r="13"/><circle cx="236" cy="130" r="13"/>
      </g>
      <g stroke="#7c8cff" stroke-opacity=".45" stroke-width="1.2" fill="none">
        <rect x="24" y="158" width="34" height="14" rx="3"/><rect x="72" y="158" width="34" height="14" rx="3"/>
        <rect x="120" y="158" width="34" height="14" rx="3"/><path d="M58 165h14M106 165h14"/>
      </g>
    </svg>"""


def _svg_github() -> str:
    return f"""
    <div style="display:grid;place-items:center;height:100%;background:#111319;color:#252934">
      <div style="width:84px;opacity:.9">{ICON_GITHUB.replace('width="20" height="20"', 'width="84" height="84"')}</div>
    </div>"""


def _card(cover: str, category: str, title: str, desc: str, tags: list[str], links: list[tuple[str, str]]) -> str:
    chips = "".join(f'<span class="chip tech">{esc(t)}</span>' for t in tags)
    anchors = "".join(
        f'<a class="link-arrow" href="{esc(url)}" target="_blank" rel="noopener noreferrer">{esc(label)} <span class="arr">→</span></a>'
        for label, url in links if is_set(url))
    return f"""
    <article class="card">
      <div class="card-media">{cover}</div>
      <div class="card-body">
        <p class="cat">{esc(category)}</p>
        <h3>{esc(title)}</h3>
        <p class="desc">{esc(desc)}</p>
        <div class="chips">{chips}</div>
        <div class="card-links">{anchors}</div>
      </div>
    </article>"""


def _other_projects() -> str:
    cards = _card(
        _svg_automata(), "Theory of Computation", "Regex to DFA + NFA to DFA simulator",
        "Two Java console tools for Formal Languages and Automata Theory: regex to minimized DFA, and NFA to DFA, "
        "both with custom string testing.",
        ["Java", "Automata theory", "Subset construction", "DFA minimization"],
        [("GitHub", TOC_REPO_URL)])
    cards += _card(
        _svg_structures(), "CS fundamentals", "Data Structures in Python",
        "Data structures written from scratch while learning them, from the basics upward.",
        ["Python", "Data structures", "Algorithms"],
        [("GitHub", DATA_STRUCTURES_REPO_URL)])
    cards += _card(
        _svg_github(), "More", "Everything else on GitHub",
        "Smaller experiments and coursework live here as they're published.",
        ["Python", "Java", "Jupyter"],
        [("Browse repositories", GITHUB_URL)])
    return f'<h3 class="sub-title">More work</h3><div class="cards">{cards}</div>'


def render_projects() -> None:
    render(f"""
    <div class="yp">
      <section class="sec" id="projects">
        <div class="wrap">
          <div class="sec-head reveal">
            <h2 class="sec-title">What I've built.</h2>
            <p class="sec-sub">One AI project I'm proud of, and the computer science underneath it.</p>
          </div>
          {_study_buddy()}
          {_other_projects()}
        </div>
      </section>
    </div>
    """)
