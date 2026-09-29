"""
Everything you may want to edit lives in this one file.

Rules of thumb
- A value that starts with "YOUR_" or is an empty string is treated as "not set".
  Buttons that depend on it are hidden (or disabled) instead of pointing nowhere.
- Nothing in here is required for the app to run.
"""

# ---------------------------------------------------------------- identity
FULL_NAME = "Youssef Abady Mohamed"
DISPLAY_NAME = "Youssef Abady"
TITLE = "AI/ML Engineer"
LOCATION = "Alexandria, Egypt"
YEAR = 2026

META_DESCRIPTION = (
    "Youssef Abady is a Computer Science student at Alexandria University "
    "building practical AI systems with machine learning, NLP, generative AI and RAG."
)

# ---------------------------------------------------------------- contact links
GITHUB_URL = "https://github.com/youssefabady-7"
LINKEDIN_URL = "https://www.linkedin.com/in/youssef-abady-8854ys/"

# TODO: add your public email. Leave empty and the Email buttons are hidden.
EMAIL = ""  # e.g. "you@example.com"

# ---------------------------------------------------------------- Study Buddy
STUDY_BUDDY_DEMO_URL = "https://stadybuddy77.streamlit.app/"
STUDY_BUDDY_GITHUB_URL = "https://github.com/youssefabady-7/Study-Buddy"

# Study Buddy was built by a team (see the repo README credits).
STUDY_BUDDY_TEAM = ["Mohamed Mahmoud", "Merna Mohamed", "Ranya Farrag"]

# TODO: one or two honest sentences about YOUR part of Study Buddy.
# Recruiters will ask. Leave empty and the "My part" block is hidden.
STUDY_BUDDY_MY_ROLE = ""
# e.g. "I worked on the retrieval pipeline and the quiz generator."

# ---------------------------------------------------------------- certificate
# Optional public verification / Credly-style link. Empty = the button opens the
# certificate image in a lightbox instead.
CERTIFICATE_URL = ""
CERTIFICATE_ISSUE_DATE = "5 Sep 2026"  # printed on the certificate

# ---------------------------------------------------------------- other projects
TOC_REPO_URL = "https://github.com/youssefabady-7/TOCFINALPROJECT-"
DATA_STRUCTURES_REPO_URL = "https://github.com/youssefabady-7/Data-structure"

# ---------------------------------------------------------------- skills
# Skills marked "used" get a small accent dot: they appear in a public project.
SKILLS = [
    {
        "title": "AI & Machine Learning",
        "items": [
            "Machine Learning",
            "Deep Learning Fundamentals",
            "Natural Language Processing",
            "Generative AI",
            "RAG",
            "AI Agents",
            "LLM Applications",
            "Prompt Engineering",
        ],
    },
    {
        "title": "AI Engineering",
        "items": [
            "Embeddings",
            "Vector Search",
            "FAISS",
            "API Integration",
            "Model Integration",
            "AI Application Development",
        ],
    },
    {
        "title": "Programming",
        "items": [
            "Python",
            "Java",
            "C++",
            "Object-Oriented Programming",
            "Data Structures & Algorithms",
        ],
    },
    {
        "title": "Data & ML Tools",
        "items": [
            "NumPy",
            "Pandas",
            "Scikit-learn",
            "TensorFlow",
            "Sentence Transformers",
        ],
    },
    {
        "title": "Development",
        "items": ["Streamlit", "Git", "GitHub", "HTML", "CSS", "JavaScript"],
    },
]

USED_IN_PROJECTS = {
    "RAG",
    "LLM Applications",
    "Embeddings",
    "Vector Search",
    "FAISS",
    "API Integration",
    "AI Application Development",
    "Python",
    "Java",
    "Data Structures & Algorithms",
    "Sentence Transformers",
    "Streamlit",
    "Git",
    "GitHub",
}

# ---------------------------------------------------------------- currently exploring
EXPLORING = [
    "Advanced Machine Learning",
    "NLP",
    "Generative AI",
    "AI Agents",
    "RAG architectures",
    "Model evaluation",
    "Production AI systems",
]
