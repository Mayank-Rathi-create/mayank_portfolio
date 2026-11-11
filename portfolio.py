"""Streamlit portfolio application.

Run with ``streamlit run portfolio.py``.
Keep the requirements minimal: add ``streamlit`` to requirements.txt.
The app is suitable for GitHub and Python hosting.

To update the site after deployment, edit PROFILE or PROJECTS, commit the
change, and redeploy.
"""

import streamlit as st
from pathlib import Path
import base64


# ============================================================
# DATA SECTION (PRESERVED EXACTLY AS ORIGINAL)
# ============================================================

PROFILE = {
    "name": "Mayank Rathi",
    "role": "CSE student building toward a career in cybersecurity.",
    "bio": (
        "First-year Computer Science Engineering student with a focus on "
        "cybersecurity. Currently learning Python, C, and the fundamentals "
        "of how systems work, and building hands-on projects as I go."
    ),
    "focus_areas": [
        "Vibe coding",
        "Python",
        "C",
        "Streamlit",
        "problem solving",
        "web security",
        "networking fundamentals",
        "Data structures and algorithms",
    ],
    "email": "mayankrathinp@gmail.com",
    "github": "https://github.com/Mayank-Rathi-create",
    "Instagram": "https://www.instagram.com/mayank_rathi11/",
    "discord": "https://discord.com/channels/@mayankrathi0719",
    "linkedin": "https://www.linkedin.com/in/mayank-rathi-555007427/",
}

PROJECTS = [
    {
        "title": "Mayuri printers",
        "description": "A web app that allows users to order customized printed products online, and see the products avilable in that printing factory.",
        "stack": "Typescript, CSS, HTML",
        "url": "https://mayuri-printers.vercel.app/"
    },
    {
        "title": "URL Checker",
        "description": "A URL checker that checks if a URL is safe to visit or not by comparying it with the original and verified URL's and using AI",
        "stack": "Python, Streamlit",
        "url": "https://mayank-portfolio.streamlit.app/"
    },
    {
        "title": "Road Watch",
        "description": "A web app designed to improve road safety by reporting hazardous conditions and alerting municipal authorities to potential dangers.",
        "stack": "Python, Streamlit",
        "url": "https://fix-potholes.streamlit.app/"
    },
    {
        "title": "Portfolio website",
        "description": "A personal portfolio website to showcase my projects, skills, and professional background.",
        "stack": "Python, Streamlit",
        "url": "https://mayank-portfolio.streamlit.app/"
    },
    {
        "title": "Number guessing game",
        "description": "A simple interactive Python game that narrows down a hidden number using guess-and-check logic.",
        "stack": "Python",
        "url": "https://github.com/Mayank-Rathi-create/number_guess.git"
    },
]

BLOGS = [
    {
        "title": "DSA learning",
        "date": "September 2026",
        "excerpt": "I am currently doing DSA practice on LeetCode and exploring the fundamentals of data structures and algorithms.",
        "tags": ["DSA", "LeetCode", "Problem Solving"],
    },
    {
        "title": "Computer Networking Basics",
        "date": "September 2026",
        "excerpt": "I am currently learning the basics of computer networking and exploring the fundamentals of cybersecurity.",
        "tags": ["Networking", "Cybersecurity"],
    },
    {
        "title": "C and Python Programming",
        "date": "September 2026",
        "excerpt": "I am currently learning the C and Python programming languages and exploring their applications in system-level programming.",
        "tags": ["C", "Python", "Programming"],
    },
]


# Session state initialization
if "projects" not in st.session_state:
    st.session_state.projects = [project.copy() for project in PROJECTS]

if "blogs" not in st.session_state:
    st.session_state.blogs = [blog.copy() for blog in BLOGS]


# Page configuration
st.set_page_config(
    page_title=f"{PROFILE['name']} — Portfolio",
    page_icon="✦",
    layout="wide",
    initial_sidebar_state="collapsed",
)


# Official platform SVG icons
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


# ============================================================
# MINIMALIST STORY-DRIVEN DESIGN SYSTEM (CSS)
# ============================================================
st.html(
    """
<style>
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:ital,wght@0,300;0,400;0,500;0,600;0,700;1,400&family=Space+Grotesk:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500;600&display=swap');

/* CSS Reset & Core Theme */
:root {
    --bg-main: #090a0f;
    --bg-surface: #11131a;
    --bg-surface-elevated: #161a24;
    --border-subtle: rgba(255, 255, 255, 0.08);
    --border-hover: rgba(255, 255, 255, 0.22);
    --text-headline: #f8fafc;
    --text-body: #94a3b8;
    --text-muted: #64748b;
    --accent-cyan: #38bdf8;
    --accent-indigo: #818cf8;
    --accent-emerald: #34d399;
    --font-sans: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif;
    --font-display: 'Space Grotesk', sans-serif;
    --font-mono: 'JetBrains Mono', monospace;
}

/* Streamlit Chrome Cleaner */
#MainMenu, header, footer {
    visibility: hidden !important;
    height: 0 !important;
}

.stApp {
    background-color: var(--bg-main) !important;
    color: var(--text-body) !important;
    font-family: var(--font-sans) !important;
    letter-spacing: -0.01em;
}

.block-container {
    max-width: 940px !important;
    padding-top: 2.2rem !important;
    padding-bottom: 5rem !important;
    padding-left: 1.5rem !important;
    padding-right: 1.5rem !important;
}

/* Ambient Background Texture */
.stApp::before {
    content: "";
    position: fixed;
    top: 0;
    left: 0;
    width: 100vw;
    height: 100vh;
    background: radial-gradient(circle at 18% 12%, rgba(56, 189, 248, 0.04) 0%, transparent 45%),
                radial-gradient(circle at 85% 65%, rgba(129, 140, 248, 0.03) 0%, transparent 50%);
    pointer-events: none;
    z-index: 0;
}

/* Top Dossier Bar */
.dossier-bar {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding-bottom: 1.4rem;
    margin-bottom: 3.2rem;
    border-bottom: 1px solid var(--border-subtle);
    font-family: var(--font-mono);
    font-size: 0.78rem;
    color: var(--text-muted);
    text-transform: uppercase;
    letter-spacing: 0.08em;
}

.status-live {
    display: inline-flex;
    align-items: center;
    gap: 0.45rem;
    color: var(--accent-emerald);
}

.status-dot {
    width: 7px;
    height: 7px;
    background: var(--accent-emerald);
    border-radius: 50%;
    box-shadow: 0 0 10px var(--accent-emerald);
    animation: pulse-dot 2.4s infinite ease-in-out;
}

@keyframes pulse-dot {
    0%, 100% { opacity: 1; transform: scale(1); }
    50% { opacity: 0.4; transform: scale(0.85); }
}

/* Section Headers */
.section-title {
    font-family: var(--font-display);
    font-size: clamp(1.6rem, 3.5vw, 2.2rem);
    font-weight: 600;
    color: var(--text-headline);
    margin: 0 0 0.6rem 0;
    letter-spacing: -0.03em;
    line-height: 1.15;
}

.section-subtitle {
    color: var(--text-muted);
    font-size: 0.95rem;
    margin-bottom: 2rem;
    line-height: 1.6;
}

/* Hero Section */
.hero-container {
    margin-bottom: 4rem;
}

.hero-name {
    font-family: var(--font-display);
    font-size: clamp(2.4rem, 6vw, 4.2rem);
    font-weight: 700;
    color: var(--text-headline);
    line-height: 1.05;
    letter-spacing: -0.035em;
    margin: 0 0 0.8rem 0;
}

.hero-role-lead {
    font-size: 1.25rem;
    color: var(--accent-cyan);
    font-weight: 500;
    line-height: 1.45;
    margin-bottom: 1.5rem;
}

.story-card {
    background: var(--bg-surface);
    border: 1px solid var(--border-subtle);
    border-radius: 14px;
    padding: 1.6rem 1.8rem;
    margin-bottom: 1.8rem;
    position: relative;
}

.story-card::before {
    content: "";
    position: absolute;
    top: 0;
    left: 0;
    width: 3px;
    height: 100%;
    background: linear-gradient(180deg, var(--accent-cyan), transparent);
    border-radius: 14px 0 0 14px;
}

.story-text {
    font-size: 1.05rem;
    line-height: 1.75;
    color: #cbd5e1;
    margin: 0;
}

/* Focus Areas */
.focus-label {
    font-family: var(--font-mono);
    font-size: 0.72rem;
    color: var(--text-muted);
    text-transform: uppercase;
    letter-spacing: 0.1em;
    margin-bottom: 0.7rem;
}

.pills-container {
    display: flex;
    flex-wrap: wrap;
    gap: 0.5rem;
    margin-bottom: 2rem;
}

.pill-item {
    font-family: var(--font-mono);
    font-size: 0.78rem;
    color: #e2e8f0;
    background: rgba(255, 255, 255, 0.03);
    border: 1px solid var(--border-subtle);
    padding: 0.32rem 0.75rem;
    border-radius: 6px;
    transition: all 0.2s ease;
}

.pill-item:hover {
    border-color: var(--accent-cyan);
    background: rgba(56, 189, 248, 0.08);
    color: var(--accent-cyan);
    transform: translateY(-1px);
}

/* Action Nav Bar */
.nav-actions {
    display: flex;
    flex-wrap: wrap;
    gap: 0.65rem;
}

.action-btn {
    display: inline-flex;
    align-items: center;
    gap: 0.55rem;
    background: var(--bg-surface);
    color: #e2e8f0 !important;
    border: 1px solid var(--border-subtle);
    padding: 0.55rem 1.15rem;
    border-radius: 8px;
    font-size: 0.84rem;
    font-weight: 500;
    text-decoration: none !important;
    transition: all 0.2s cubic-bezier(0.16, 1, 0.3, 1);
}

.action-btn svg {
    flex-shrink: 0;
    transition: transform 0.2s ease;
}

.action-btn:hover {
    background: var(--bg-surface-elevated);
    border-color: var(--border-hover);
    color: #ffffff !important;
    transform: translateY(-2px);
    box-shadow: 0 6px 18px rgba(0, 0, 0, 0.4);
}

.action-btn:hover svg {
    transform: scale(1.1);
}

/* =========================
   PROJECT CARDS
   ========================= */
.project-grid {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 1.5rem;
    margin-bottom: 4.5rem;
}

@media (max-width: 720px) {
    .project-grid {
        grid-template-columns: 1fr;
    }
}

.project-card {
    background: var(--bg-surface);
    border: 1px solid var(--border-subtle);
    border-radius: 16px;
    padding: 1.85rem;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    transition: all 0.28s cubic-bezier(0.16, 1, 0.3, 1);
    position: relative;
    text-decoration: none !important;
    box-sizing: border-box;
    min-height: 210px;
}

.project-card:hover {
    background: var(--bg-surface-elevated);
    border-color: var(--border-hover);
    transform: translateY(-4px);
    box-shadow: 0 16px 36px -10px rgba(0, 0, 0, 0.55), 0 0 25px rgba(56, 189, 248, 0.05);
}

.project-title {
    font-family: var(--font-display);
    font-size: 1.35rem;
    font-weight: 600;
    color: var(--text-headline);
    margin: 0 0 0.85rem 0;
    letter-spacing: -0.02em;
    line-height: 1.25;
}

.project-brief {
    font-size: 0.92rem;
    line-height: 1.65;
    color: var(--text-body);
    margin-bottom: 1.6rem;
    flex-grow: 1;
}

.project-footer {
    border-top: 1px solid var(--border-subtle);
    padding-top: 1.1rem;
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.project-stack-tags {
    font-family: var(--font-mono);
    font-size: 0.75rem;
    color: var(--text-muted);
}

.project-link-action {
    display: inline-flex;
    align-items: center;
    gap: 0.35rem;
    font-family: var(--font-mono);
    font-size: 0.78rem;
    font-weight: 500;
    color: #f8fafc;
    transition: gap 0.2s ease, color 0.2s ease;
}

.project-card:hover .project-link-action {
    color: var(--accent-cyan);
    gap: 0.6rem;
}

/* =========================
   FIELD NOTES / UPDATES
   ========================= */
.chronicle-timeline {
    display: flex;
    flex-direction: column;
    gap: 1.25rem;
    margin-bottom: 4.5rem;
    position: relative;
}

.chronicle-item {
    background: var(--bg-surface);
    border: 1px solid var(--border-subtle);
    border-left: 2px solid var(--accent-cyan);
    border-radius: 0 14px 14px 0;
    padding: 1.5rem 1.8rem;
    transition: all 0.25s ease;
}

.chronicle-item:hover {
    background: var(--bg-surface-elevated);
    border-color: var(--border-hover);
    border-left-color: #38bdf8;
    transform: translateX(4px);
}

.chronicle-meta {
    margin-bottom: 0.65rem;
}

.chronicle-date {
    font-family: var(--font-mono);
    font-size: 0.72rem;
    color: var(--accent-cyan);
    letter-spacing: 0.08em;
    text-transform: uppercase;
}

.chronicle-title {
    font-family: var(--font-display);
    font-size: 1.2rem;
    font-weight: 600;
    color: var(--text-headline);
    margin: 0 0 0.65rem 0;
    letter-spacing: -0.015em;
}

.chronicle-excerpt {
    font-size: 0.92rem;
    line-height: 1.65;
    color: var(--text-body);
    margin-bottom: 0.95rem;
}

.chronicle-tags {
    display: flex;
    flex-wrap: wrap;
    gap: 0.4rem;
}

.chronicle-tag-pill {
    font-family: var(--font-mono);
    font-size: 0.7rem;
    color: var(--text-muted);
    background: rgba(255, 255, 255, 0.02);
    border: 1px solid var(--border-subtle);
    padding: 0.18rem 0.55rem;
    border-radius: 4px;
}

/* =========================
   CONTACT
   ========================= */
.contact-card {
    background: var(--bg-surface);
    border: 1px solid var(--border-subtle);
    border-radius: 18px;
    padding: 2.3rem;
    margin-bottom: 4rem;
    text-align: left;
    position: relative;
    overflow: hidden;
}

.contact-card::before {
    content: "";
    position: absolute;
    top: -60px;
    right: -60px;
    width: 140px;
    height: 140px;
    background: radial-gradient(circle, rgba(56, 189, 248, 0.12), transparent 70%);
    pointer-events: none;
}

.contact-pitch {
    font-size: 1.05rem;
    line-height: 1.7;
    color: var(--text-body);
    margin-bottom: 2rem;
    max-width: 620px;
}

.contact-channels {
    display: flex;
    flex-wrap: wrap;
    gap: 0.85rem;
}

/* Editorial Colophon / Footer */
.colophon {
    border-top: 1px solid var(--border-subtle);
    padding-top: 2rem;
    display: flex;
    justify-content: space-between;
    align-items: center;
    font-family: var(--font-mono);
    font-size: 0.75rem;
    color: var(--text-muted);
    letter-spacing: 0.02em;
}

@media (max-width: 600px) {
    .colophon {
        flex-direction: column;
        gap: 0.75rem;
        align-items: flex-start;
    }
}
</style>
"""
)


# ============================================================
# TOP BAR
# ============================================================
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


# ============================================================
# HERO SECTION (WITHOUT PHOTO)
# ============================================================
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
        <a href="{PROFILE['Instagram']}" target="_blank" rel="noopener noreferrer" class="action-btn">{ICONS['instagram']}<span>Instagram</span> ↗</a>
        <a href="{PROFILE['linkedin']}" target="_blank" rel="noopener noreferrer" class="action-btn">{ICONS['linkedin']}<span>LinkedIn</span> ↗</a>
    </div>
</div>
"""
st.html(hero_section_html)


# ============================================================
# PROJECTS
# ============================================================
st.html(
    """
<h2 class="section-title">Projects</h2>
<div class="section-subtitle">Prototypes and systems built with focused problem solving and clean implementations.</div>
"""
)

# Render projects in a structured, clean grid without case numbers or badges
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

grid_wrapper_html = f"""
<div class="project-grid">
{''.join(project_cards_html)}
</div>
"""
st.html(grid_wrapper_html)


# ============================================================
# WHAT I'M UP TO
# ============================================================
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

chronicle_wrapper_html = f"""
<div class="chronicle-timeline">
{''.join(chronicle_items_html)}
</div>
"""
st.html(chronicle_wrapper_html)


# ============================================================
# CONTACT
# ============================================================
st.html(
    """
<h2 class="section-title">Let's work together</h2>
"""
)

contact_section_html = f"""
<div class="contact-card">
    <p class="contact-pitch">
        If you have a project in mind or just want to say hi, feel free to reach out!
    </p>
    <div class="contact-channels">
        <a href="mailto:{PROFILE['email']}" class="action-btn">{ICONS['email']}<span>Email me</span> ↗</a>
        <a href="{PROFILE['github']}" target="_blank" rel="noopener noreferrer" class="action-btn">{ICONS['github']}<span>GitHub</span> ↗</a>
        <a href="{PROFILE['discord']}" target="_blank" rel="noopener noreferrer" class="action-btn">{ICONS['discord']}<span>Discord</span> ↗</a>
        <a href="{PROFILE['Instagram']}" target="_blank" rel="noopener noreferrer" class="action-btn">{ICONS['instagram']}<span>Instagram</span> ↗</a>
        <a href="{PROFILE['linkedin']}" target="_blank" rel="noopener noreferrer" class="action-btn">{ICONS['linkedin']}<span>LinkedIn</span> ↗</a>
    </div>
</div>
"""
st.html(contact_section_html)


# ============================================================
# FOOTER / COLOPHON
# ============================================================
st.html(
    f"""
<div class="colophon">
    <div>© 2026 {PROFILE['name']} · Built with Python and Streamlit</div>
    <div>PORTFOLIO ARCHIVE</div>
</div>
"""
)
