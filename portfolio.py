"""Streamlit Portfolio Application.

Can be run locally with:
    streamlit run portfolio.py

Data is cleanly separated in `data/portfolio.json` and styles in `css/style.css`.
"""

import json
from pathlib import Path
import streamlit as st

# Paths
BASE_DIR = Path(__file__).parent
DATA_FILE = BASE_DIR / "data" / "portfolio.json"
CSS_FILE = BASE_DIR / "css" / "style.css"

# Load Data
with open(DATA_FILE, "r", encoding="utf-8") as f:
    DATA = json.load(f)

PROFILE = DATA["profile"]
PROJECTS = DATA["projects"]
BLOGS = DATA["blogs"]

# Session State Initialization
if "projects" not in st.session_state:
    st.session_state.projects = [p.copy() for p in PROJECTS]

if "blogs" not in st.session_state:
    st.session_state.blogs = [b.copy() for b in BLOGS]

# Page Configuration
st.set_page_config(
    page_title=f"{PROFILE['name']} — Portfolio",
    page_icon="✦",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# SVG Icons
ICONS = {
    "email": (
        '<svg width="15" height="15" viewBox="0 0 24 24" fill="none" '
        'stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">'
        '<rect width="20" height="16" x="2" y="4" rx="2"></rect>'
        '<path d="m22 7-8.97 5.7a1.94 1.94 0 0 1-2.06 0L2 7"></path></svg>'
    ),
    "github": (
        '<svg width="15" height="15" viewBox="0 0 24 24" fill="currentColor">'
        '<path d="M12 0C5.37 0 0 5.37 0 12c0 5.31 3.435 9.795 8.205 11.385.6.105.825-.255.825-.57 0-.285-.015-1.23-.015-2.235-3.015.555-3.795-.735-4.035-1.41-.135-.345-.72-1.41-1.23-1.695-.42-.225-1.02-.78-.015-.795.945-.015 1.62.87 1.845 1.23 1.08 1.815 2.805 1.305 3.495.99.105-.78.42-1.305.765-1.605-2.67-.3-5.46-1.335-5.46-5.925 0-1.305.465-2.385 1.23-3.225-.12-.3-.54-1.53.12-3.18 0 0 1.005-.315 3.3 1.23.96-.27 1.98-.405 3-.405s2.04.135 3 .405c2.295-1.56 3.3-1.23 3.3-1.23.66 1.65.24 2.88.12 3.18.765.84 1.23 1.905 1.23 3.225 0 4.605-2.805 5.625-5.475 5.925.435.375.81 1.095.81 2.22 0 1.605-.015 2.895-.015 3.3 0 .315.225.69.825.57A12.02 12.02 0 0 0 24 12c0-6.63-5.37-12-12-12z"/>'
        '</svg>'
    ),
    "discord": (
        '<svg width="15" height="15" viewBox="0 0 24 24" fill="currentColor">'
        '<path d="M20.317 4.37a19.791 19.791 0 0 0-4.885-1.515.074.074 0 0 0-.079.037c-.21.375-.444.864-.608 1.25a18.27 18.27 0 0 0-5.487 0 12.64 12.64 0 0 0-.617-1.25.077.077 0 0 0-.079-.037A19.736 19.736 0 0 0 3.677 4.37a.07.07 0 0 0-.032.027C.533 9.046-.32 13.58.099 18.057a.082.082 0 0 0 .031.057 19.9 19.9 0 0 0 5.993 3.03.078.078 0 0 0 .084-.028c.462-.63.874-1.295 1.226-1.994.021-.041.001-.09-.041-.106a13.107 13.107 0 0 1-1.872-.892.077.077 0 0 1-.008-.128 10.2 10.2 0 0 0 .372-.292.074.074 0 0 1 .077-.01c3.928 1.793 8.18 1.793 12.061 0a.074.074 0 0 1 .078.01c.12.098.246.198.373.292a.077.077 0 0 1-.006.127 12.299 12.299 0 0 1-1.873.893.077.077 0 0 0-.041.107c.36.698.772 1.362 1.225 1.993a.076.076 0 0 0 .084.028 19.839 19.839 0 0 0 6.002-3.03.077.077 0 0 0 .032-.054c.5-5.177-.838-9.674-3.549-13.66a.061.061 0 0 0-.031-.028zM8.02 15.33c-1.183 0-2.157-1.085-2.157-2.419 0-1.333.956-2.419 2.157-2.419 1.21 0 2.176 1.096 2.157 2.42 0 1.333-.956 2.418-2.157 2.418zm7.975 0c-1.183 0-2.157-1.085-2.157-2.419 0-1.333.955-2.419 2.157-2.419 1.21 0 2.176 1.096 2.157 2.42 0 1.333-.946 2.418-2.157 2.418z"/>'
        '</svg>'
    ),
    "instagram": (
        '<svg width="15" height="15" viewBox="0 0 24 24" fill="none" '
        'stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">'
        '<rect width="20" height="20" x="2" y="2" rx="5" ry="5"></rect>'
        '<path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z"></path>'
        '<line x1="17.5" x2="17.51" y1="6.5" y2="6.5"></line></svg>'
    ),
    "linkedin": (
        '<svg width="15" height="15" viewBox="0 0 24 24" fill="currentColor">'
        '<path d="M19 0h-14c-2.761 0-5 2.239-5 5v14c0 2.761 2.239 5 5 5h14c2.762 0 5-2.239 5-5v-14c0-2.761-2.238-5-5-5zm-11 19h-3v-11h3v11zm-1.5-12.268c-.966 0-1.75-.79-1.75-1.764s.784-1.764 1.75-1.764 1.75.79 1.75 1.764-.783 1.764-1.75 1.764zm13.5 12.268h-3v-5.604c0-3.368-4-3.113-4 0v5.604h-3v-11h3v1.765c1.396-2.586 7-2.777 7 2.476v6.759z"/>'
        '</svg>'
    ),
}

# Inject External CSS
with open(CSS_FILE, "r", encoding="utf-8") as f:
    st.html(f"<style>{f.read()}</style>")

# 1. Top Bar
st.html(
    """
<div class="dossier-bar">
    <div>PORTFOLIO // 2026</div>
    <div class="status-live">
        <span class="status-dot"></span>
        <span>AVAILABLE &amp; BUILDING</span>
    </div>
</div>
"""
)

# 2. Hero Section
focus_pills_html = "".join(
    f'<span class="pill-item">{skill}</span>' for skill in PROFILE["focus_areas"]
)

hero_section_html = f"""
<div class="hero-container">
    <h1 class="hero-name">Hi, I'm {PROFILE['name']}.</h1>
    <div class="hero-role-lead">{PROFILE['role']}</div>
    
    <div class="story-card">
        <p class="story-text">{PROFILE['bio']}</p>
    </div>

    <div class="focus-label">FOCUS AREAS &amp; EXPLORATIONS</div>
    <div class="pills-container">
        {focus_pills_html}
    </div>

    <div class="nav-actions">
        <a href="mailto:{PROFILE['email']}" class="action-btn">{ICONS['email']}<span>Email</span> ↗</a>
        <a href="{PROFILE['github']}" target="_blank" rel="noopener noreferrer" class="action-btn">{ICONS['github']}<span>GitHub</span> ↗</a>
        <a href="{PROFILE['discord']}" target="_blank" rel="noopener noreferrer" class="action-btn">{ICONS['discord']}<span>Discord</span> ↗</a>
        <a href="{PROFILE['instagram']}" target="_blank" rel="noopener noreferrer" class="action-btn">{ICONS['instagram']}<span>Instagram</span> ↗</a>
        <a href="{PROFILE['linkedin']}" target="_blank" rel="noopener noreferrer" class="action-btn">{ICONS['linkedin']}<span>LinkedIn</span> ↗</a>
    </div>
</div>
"""
st.html(hero_section_html)

# 3. Projects Section
st.html(
    """
<h2 class="section-title">Projects</h2>
<div class="section-subtitle">Prototypes and systems built with focused problem solving and clean implementations.</div>
"""
)

project_cards_html = []
for project in st.session_state.projects:
    card_html = f"""
    <a href="{project['url']}" target="_blank" rel="noopener noreferrer" class="project-card">
        <div>
            <h3 class="project-title">{project['title']}</h3>
            <p class="project-brief">{project['description']}</p>
        </div>
        <div class="project-footer">
            <span class="project-stack-tags">{project['stack']}</span>
            <span class="project-link-action">View project ↗</span>
        </div>
    </a>
    """
    project_cards_html.append(card_html)

st.html(f'<div class="project-grid">{"".join(project_cards_html)}</div>')

# 4. What I'm up to (Chronicle)
st.html(
    """
<h2 class="section-title">What I'm up to</h2>
<div class="section-subtitle">Ongoing dispatches, concepts under exploration, and engineering milestones.</div>
"""
)

chronicle_items_html = []
for blog in st.session_state.blogs:
    tag_pills = "".join(f'<span class="chronicle-tag-pill">{tag}</span>' for tag in blog["tags"])
    entry_html = f"""
    <div class="chronicle-item">
        <div class="chronicle-meta">
            <span class="chronicle-date">{blog['date']}</span>
        </div>
        <h3 class="chronicle-title">{blog['title']}</h3>
        <p class="chronicle-excerpt">{blog['excerpt']}</p>
        <div class="chronicle-tags">{tag_pills}</div>
    </div>
    """
    chronicle_items_html.append(entry_html)

st.html(f'<div class="chronicle-timeline">{"".join(chronicle_items_html)}</div>')

# 5. Contact Section
st.html('<h2 class="section-title">Let\'s work together</h2>')

contact_section_html = f"""
<div class="contact-card">
    <p class="contact-pitch">
        If you have a project in mind or just want to say hi, feel free to reach out!
    </p>
    <div class="contact-channels">
        <a href="mailto:{PROFILE['email']}" class="action-btn">{ICONS['email']}<span>Email me</span> ↗</a>
        <a href="{PROFILE['github']}" target="_blank" rel="noopener noreferrer" class="action-btn">{ICONS['github']}<span>GitHub</span> ↗</a>
        <a href="{PROFILE['discord']}" target="_blank" rel="noopener noreferrer" class="action-btn">{ICONS['discord']}<span>Discord</span> ↗</a>
        <a href="{PROFILE['instagram']}" target="_blank" rel="noopener noreferrer" class="action-btn">{ICONS['instagram']}<span>Instagram</span> ↗</a>
        <a href="{PROFILE['linkedin']}" target="_blank" rel="noopener noreferrer" class="action-btn">{ICONS['linkedin']}<span>LinkedIn</span> ↗</a>
    </div>
</div>
"""
st.html(contact_section_html)

# 6. Footer
st.html(
    f"""
<div class="colophon">
    <div>© 2026 {PROFILE['name']} · Built with Python and modern web standards</div>
    <div>PORTFOLIO ARCHIVE</div>
</div>
"""
)
