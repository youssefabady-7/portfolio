"""Education timeline + HCIA-AI certificate card (with a no-JS lightbox)."""
from yp_config import CERTIFICATE_ISSUE_DATE, CERTIFICATE_URL
from yp_helpers import esc, img_uri, is_set, render

FOUNDATIONS = ["Programming", "Algorithms", "Data Structures", "Mathematics", "Statistics",
               "Software development", "CS fundamentals"]
CERT_TOPICS = ["Machine Learning", "Deep Learning", "NLP", "AI fundamentals", "AI development workflows"]


def _certificate() -> str:
    thumb = img_uri("hcia-ai-certificate-thumb.jpg")
    full = img_uri("hcia-ai-certificate.jpg")
    topics = "".join(f'<span class="chip">{t}</span>' for t in CERT_TOPICS)
    alt = "HCIA-AI V4.0 Course certificate of completion from Huawei ICT Academy"

    if thumb and full:
        media = f'<a class="cert-thumb" href="#certificate" aria-label="Open certificate"><img src="{thumb}" alt="{alt}"></a>'
        lightbox = f"""
        <div class="lightbox" id="certificate" role="dialog" aria-label="Certificate">
          <a class="lb-close-area" href="#cert-card" aria-label="Close certificate"></a>
          <a class="lb-x" href="#cert-card" aria-label="Close">×</a>
          <img src="{full}" alt="{alt}">
        </div>"""
        view = ('<a class="btn btn-ghost" href="#certificate">View Certificate</a>'
                if not is_set(CERTIFICATE_URL) else "")
    else:
        media = '<div class="cert-thumb"><div class="cert-ph">Add assets/hcia-ai-certificate.jpg</div></div>'
        lightbox, view = "", ""
    if is_set(CERTIFICATE_URL):
        view = (f'<a class="btn btn-ghost" href="{esc(CERTIFICATE_URL)}" target="_blank" '
                f'rel="noopener noreferrer">View Certificate</a>')

    return f"""
    <div class="cert" id="cert-card">
      {media}
      <div>
        <span class="cert-badge">Certificate of Completion</span>
        <h3>HCIA-AI V4.0 Course</h3>
        <p class="by">Huawei ICT Academy, in partnership with NTI · Issued {esc(CERTIFICATE_ISSUE_DATE)}</p>
        <div class="chips">{topics}</div>
        <div class="btn-row">{view}</div>
      </div>
    </div>
    {lightbox}"""


def render_education() -> None:
    found = "".join(f'<span class="chip">{f}</span>' for f in FOUNDATIONS)
    render(f"""
    <div class="yp">
      <section class="sec" id="education">
        <div class="wrap">
          <div class="sec-head reveal">
            <h2 class="sec-title">Where I'm learning.</h2>
          </div>
          <div class="edu-grid">
            <div class="tl">
              <div class="tl-item">
                <span class="tl-meta">2024 — 2028</span>
                <h3>Alexandria University</h3>
                <p class="where">Faculty of Science · Computer Science</p>
                <p class="note">My academic foundation. It's where the fundamentals come from.</p>
                <div class="chips">{found}</div>
              </div>
              <div class="tl-item">
                <span class="tl-meta">Egypt</span>
                <h3>Digital Egypt Pioneers Initiative (DEPI)</h3>
                <p class="where">AI/ML-focused training</p>
              </div>
            </div>
            {_certificate()}
          </div>
        </div>
      </section>
    </div>
    """)
