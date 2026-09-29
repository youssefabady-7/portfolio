"""Youssef Abady: AI/ML Engineer portfolio.

Deliberately flat: every file lives at the repo root (no subfolders except assets/ and
.streamlit/). GitHub's drag-and-drop uploader has repeatedly flattened subfolders for this
project, silently dropping files at the top level and breaking imports. A flat layout has
nothing left to flatten.

Run locally:   streamlit run app.py
Deploy:        push to GitHub, then create the app on share.streamlit.io (main file: app.py)
"""
import sys
from pathlib import Path

import streamlit as st

ROOT = Path(__file__).resolve().parent
if str(ROOT) not in sys.path:  # make sure files in this repo win over any same-named package
    sys.path.insert(0, str(ROOT))

from yp_config import DISPLAY_NAME, TITLE  # noqa: E402

_icon = ROOT / "assets" / "favicon.png"

# Must be the first Streamlit call.
st.set_page_config(
    page_title=f"{DISPLAY_NAME} | {TITLE}",
    page_icon=str(_icon) if _icon.is_file() else "🧠",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Fail with a readable message (instead of a redacted traceback) if a file didn't reach GitHub.
_REQUIRED = [
    "yp_config.py", "yp_helpers.py", "yp_styles.py", "yp_browser.py", "yp_nav.py", "yp_hero.py",
    "yp_about.py", "yp_skills.py", "yp_projects.py", "yp_process.py", "yp_education.py",
    "yp_contact.py", "yp_footer.py",
]
_missing = [f for f in _REQUIRED if not (ROOT / f).is_file()]
if _missing:
    st.error(
        "These files are missing from the repository: " + ", ".join(_missing) + ". "
        "Upload them to the repo root (same level as app.py, not inside a folder), then reboot the app."
    )
    st.stop()

import yp_browser as browser  # noqa: E402
from yp_about import render_about  # noqa: E402
from yp_contact import render_contact  # noqa: E402
from yp_education import render_education  # noqa: E402
from yp_footer import render_footer  # noqa: E402
from yp_helpers import render  # noqa: E402
from yp_hero import render_hero  # noqa: E402
from yp_nav import render_nav  # noqa: E402
from yp_process import render_exploring, render_process  # noqa: E402
from yp_projects import render_projects  # noqa: E402
from yp_skills import render_skills  # noqa: E402
from yp_styles import CSS  # noqa: E402

render(CSS)          # design system
render_nav()         # sticky navigation
render_hero()        # who I am
render_about()       # how I think
render_skills()      # what I work with
render_projects()    # what I build (Study Buddy + more)
render_process()     # how I build it
render_education()   # what I study + certificate
render_exploring()   # what I'm learning
render_contact()     # how to reach me
render_footer()
browser.inject()     # optional: meta tags, smooth scroll, active nav
