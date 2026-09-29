# Youssef Abady — AI/ML Engineer Portfolio

A dark, minimal personal site built **entirely in Python + Streamlit** (custom HTML/CSS injected through
`st.markdown`). No API keys, no database, no build step.

**Layout is deliberately flat.** Every code file sits at the repo root — `app.py`, `yp_config.py`,
`yp_helpers.py`, `yp_styles.py`, `yp_browser.py`, and one `yp_<section>.py` per section. Only `assets/`
(images) and `.streamlit/` (theme) are folders. This is on purpose: GitHub's drag-and-drop uploader has a
habit of silently flattening subfolders, which breaks Python imports. With no subfolders to flatten, that
failure mode can't happen.

## Run locally

```bash
python -m venv .venv && source .venv/bin/activate      # Windows: .venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py
```

## Uploading to GitHub — read this first

If your repo currently has old `components/`, `utils/`, `sections/`, or `site_utils/` folders, or a
`config.py` at the root, **delete them from the repo before uploading these files.** Leftover files from an
earlier version will sit next to the new ones and can cause confusing duplicate-content or import errors.

**Safest method — a Git client (recommended):**
```bash
git clone https://github.com/<you>/<repo>.git
# delete everything inside the cloned folder except .git, then copy in all files from this zip
cd <repo>
git add -A
git commit -m "Flat layout"
git push
```
This is reliable because there's nothing left to flatten — no subfolders means no folder-structure to lose.

**Using the GitHub website instead:** Go to your repo → **Add file → Upload files** → drag in *all* the
files from this folder at once (select them all in your file browser, then drag). Do this in one drop.
Afterwards, open the repo and confirm you see `app.py`, `yp_config.py`, `yp_helpers.py`, etc. directly at the
top level (not inside any folder), plus an `assets/` folder and a `.streamlit/` folder.

## Deploy (Streamlit Community Cloud)

1. Push this folder to a GitHub repo.
2. Go to <https://share.streamlit.io> → **Create app** → pick the repo, branch, main file `app.py`.
3. Deploy. The `.streamlit/config.toml` theme is picked up automatically.
4. If you already had this app deployed, use **Manage app → Reboot app** after pushing changes.

## Where to edit things

| I want to change…                         | Edit                                      |
|-------------------------------------------|--------------------------------------------|
| Links, email, skills, "exploring" list     | `yp_config.py` (the only file most people need) |
| Section copy                               | `yp_<section>.py` (e.g. `yp_hero.py`, `yp_projects.py`) |
| Colours, fonts, spacing, animations        | `yp_styles.py` (tokens at the top: `--accent`, `--bg`, …) |
| Photo / certificate / screenshot           | `assets/`                                 |

Any config value that is empty or starts with `YOUR_` is treated as "not set": the related button is hidden
(or shown disabled) instead of pointing at nothing.

### Still to fill in (`yp_config.py`)
- `EMAIL` — Email buttons and the mail icon appear once this is set.
- `STUDY_BUDDY_MY_ROLE` — one or two honest sentences about *your* part of Study Buddy (it's a team project).
- `CERTIFICATE_URL` — optional public verification link. If empty, **View Certificate** opens the image in a lightbox.

### Assets
| File                                    | Status                                                        |
|-----------------------------------------|-----------------------------------------------------------------|
| `assets/profile.jpg`                    | Included (your photo, resized to 760 px wide).                 |
| `assets/hcia-ai-certificate.jpg` + `-thumb.jpg` | Included (from your certificate).                       |
| `assets/study-buddy.png`                | **Optional.** Drop a screenshot here and it replaces the schematic preview automatically. |
| `assets/favicon.png`                    | Included ("YA" monogram).                                       |

Keep images small (photo ≲ 100 KB, screenshot ≲ 250 KB). They are inlined as base64, so size = page weight.

## How it works

```
app.py             page config, checks every file is present, then calls each section in order
yp_config.py       all content / links / toggles
yp_<section>.py    one file per section (nav, hero, about, skills, projects, process, education, contact, footer)
yp_styles.py       the design system (one <style> block)
yp_helpers.py      image loading (cached), HTML minifier, icons
yp_browser.py      ~35 lines of optional JS: meta tags, smooth scroll, active nav link
```

Why single-line HTML? `st.markdown` runs a Markdown parser before HTML, so blank lines and 4-space indents
inside HTML would turn into code blocks. `render()` (in `yp_helpers.py`) collapses each block to one line to
avoid that.

- **No sidebar, no Streamlit chrome** — hidden with CSS.
- **Motion** is limited to: a staggered hero load, a slow drifting grid/glow, hover states, a scroll-linked
  fade on section headings (CSS `animation-timeline`, Chromium/Safari 26+; ignored elsewhere), and the flowing
  connectors in the RAG diagram. Everything is disabled under `prefers-reduced-motion`.
- **Certificate lightbox** is pure CSS (`:target`), no JavaScript.

## Things to verify after deploying
- Open the app: if a file is missing, you'll see a plain list of missing filenames instead of a Python
  traceback — re-upload those files to the repo root and reboot.
- Resize the window / open on your phone: hero → about → skills → projects → education → contact should stack cleanly.
- Click each nav item; the active link should highlight as you scroll.
- Click **Live Demo**, **View on GitHub**, **View Certificate**, and the GitHub/LinkedIn icons.

## Content notes (credibility)
- The certificate is a **Certificate of Completion** for the HCIA-AI V4.0 *course*; the certificate itself says it
  does not represent passing the Huawei certification exam. The site labels it accordingly.
- Study Buddy is credited as a **team project**, matching the repo README.
- The stack shown for Study Buddy (Groq `gpt-oss-120b`, `all-MiniLM-L6-v2`, FAISS, pypdf, Kokoro) comes from that repo's README.
- Skills with a dot are ones that appear in a public repo; the rest are listed by you and not evidenced there.
