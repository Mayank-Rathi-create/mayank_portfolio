"""Portfolio Static Site Generator.

Reads data from `data/portfolio.json` and generates `index.html` with
proper semantic markup, accessible SVG icons, and SEO metadata.

Run with:
    python build.py
"""

import json
from pathlib import Path

# Paths
BASE_DIR = Path(__file__).parent
DATA_FILE = BASE_DIR / "data" / "portfolio.json"
HTML_FILE = BASE_DIR / "index.html"

# SVGs (accessible, clean icons)
ICONS = {
    "email": (
        '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" '
        'stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'
        '<rect width="20" height="16" x="2" y="4" rx="2"></rect>'
        '<path d="m22 7-8.97 5.7a1.94 1.94 0 0 1-2.06 0L2 7"></path></svg>'
    ),
    "github": (
        '<svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">'
        '<path d="M12 0C5.37 0 0 5.37 0 12c0 5.31 3.435 9.795 8.205 11.385.6.105.825-.255.825-.57 0-.285-.015-1.23-.015-2.235-3.015.555-3.795-.735-4.035-1.41-.135-.345-.72-1.41-1.23-1.695-.42-.225-1.02-.78-.015-.795.945-.015 1.62.87 1.845 1.23 1.08 1.815 2.805 1.305 3.495.99.105-.78.42-1.305.765-1.605-2.67-.3-5.46-1.335-5.46-5.925 0-1.305.465-2.385 1.23-3.225-.12-.3-.54-1.53.12-3.18 0 0 1.005-.315 3.3 1.23.96-.27 1.98-.405 3-.405s2.04.135 3 .405c2.295-1.56 3.3-1.23 3.3-1.23.66 1.65.24 2.88.12 3.18.765.84 1.23 1.905 1.23 3.225 0 4.605-2.805 5.625-5.475 5.925.435.375.81 1.095.81 2.22 0 1.605-.015 2.895-.015 3.3 0 .315.225.69.825.57A12.02 12.02 0 0 0 24 12c0-6.63-5.37-12-12-12z"/>'
        '</svg>'
    ),
    "linkedin": (
        '<svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">'
        '<path d="M19 0h-14c-2.761 0-5 2.239-5 5v14c0 2.761 2.239 5 5 5h14c2.762 0 5-2.239 5-5v-14c0-2.761-2.238-5-5-5zm-11 19h-3v-11h3v11zm-1.5-12.268c-.966 0-1.75-.79-1.75-1.764s.784-1.764 1.75-1.764 1.75.79 1.75 1.764-.783 1.764-1.75 1.764zm13.5 12.268h-3v-5.604c0-3.368-4-3.113-4 0v5.604h-3v-11h3v1.765c1.396-2.586 7-2.777 7 2.476v6.759z"/>'
        '</svg>'
    ),
    "discord": (
        '<svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">'
        '<path d="M20.317 4.37a19.791 19.791 0 0 0-4.885-1.515.074.074 0 0 0-.079.037c-.21.375-.444.864-.608 1.25a18.27 18.27 0 0 0-5.487 0 12.64 12.64 0 0 0-.617-1.25.077.077 0 0 0-.079-.037A19.736 19.736 0 0 0 3.677 4.37a.07.07 0 0 0-.032.027C.533 9.046-.32 13.58.099 18.057a.082.082 0 0 0 .031.057 19.9 19.9 0 0 0 5.993 3.03.078.078 0 0 0 .084-.028c.462-.63.874-1.295 1.226-1.994.021-.041.001-.09-.041-.106a13.107 13.107 0 0 1-1.872-.892.077.077 0 0 1-.008-.128 10.2 10.2 0 0 0 .372-.292.074.074 0 0 1 .077-.01c3.928 1.793 8.18 1.793 12.061 0a.074.074 0 0 1 .078.01c.12.098.246.198.373.292a.077.077 0 0 1-.006.127 12.299 12.299 0 0 1-1.873.893.077.077 0 0 0-.041.107c.36.698.772 1.362 1.225 1.993a.076.076 0 0 0 .084.028 19.839 19.839 0 0 0 6.002-3.03.077.077 0 0 0 .032-.054c.5-5.177-.838-9.674-3.549-13.66a.061.061 0 0 0-.031-.028zM8.02 15.33c-1.183 0-2.157-1.085-2.157-2.419 0-1.333.956-2.419 2.157-2.419 1.21 0 2.176 1.096 2.157 2.42 0 1.333-.956 2.418-2.157 2.418zm7.975 0c-1.183 0-2.157-1.085-2.157-2.419 0-1.333.955-2.419 2.157-2.419 1.21 0 2.176 1.096 2.157 2.42 0 1.333-.946 2.418-2.157 2.418z"/>'
        '</svg>'
    ),
    "instagram": (
        '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" '
        'stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'
        '<rect width="20" height="20" x="2" y="2" rx="5" ry="5"></rect>'
        '<path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z"></path>'
        '<line x1="17.5" x2="17.51" y1="6.5" y2="6.5"></line></svg>'
    ),
    "external": (
        '<svg width="13" height="13" viewBox="0 0 24 24" fill="none" '
        'stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'
        '<path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"></path>'
        '<polyline points="15 3 21 3 21 9"></polyline>'
        '<line x1="10" y1="14" x2="21" y2="3"></line></svg>'
    ),
    "copy": (
        '<svg width="15" height="15" viewBox="0 0 24 24" fill="none" '
        'stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'
        '<rect width="14" height="14" x="8" y="8" rx="2" ry="2"></rect>'
        '<path d="M4 16c-1.1 0-2-.9-2-2V4c0-1.1.9-2 2-2h10c1.1 0 2 .9 2 2"></path></svg>'
    ),
}


def build():
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)

    profile = data["profile"]
    skills = data["skills"]
    projects = data["projects"]
    learning = data["learning_dispatches"]

    # Render Skills Categories
    prog_skills = "\n".join(
        f"""                    <li class="skill-item">
                        <span class="skill-name">{s['name']}</span>
                        <span class="skill-note">{s['note']}</span>
                    </li>"""
        for s in skills["programming"]
    )

    web_skills = "\n".join(
        f"""                    <li class="skill-item">
                        <span class="skill-name">{s['name']}</span>
                        <span class="skill-note">{s['note']}</span>
                    </li>"""
        for s in skills["web_and_tools"]
    )

    learn_skills = "\n".join(
        f"""                    <li class="skill-item">
                        <span class="skill-name">{s['name']}</span>
                        <span class="skill-note">{s['note']}</span>
                    </li>"""
        for s in skills["current_learning"]
    )

    # Render Projects Grid
    project_cards = []
    for proj in projects:
        stack_html = "".join(f'<span class="stack-tag">{t}</span>' for t in proj["stack"])
        external_badge = ""
        if proj.get("url"):
            external_badge = f"""<a href="{proj['url']}" target="_blank" rel="noopener noreferrer" class="project-link-badge" aria-label="Visit {proj['title']} (opens in new tab)">
                    <span>Visit live</span>
                    {ICONS['external']}
                </a>"""

        card_html = f"""            <article class="project-card">
                <div>
                    <div class="project-header">
                        <h3 class="project-title">{proj['title']}</h3>
                        {external_badge}
                    </div>
                    <p class="project-description">{proj['description']}</p>
                    <div class="project-demonstrates">
                        <strong>Focus:</strong> {proj['demonstrates']}
                    </div>
                </div>
                <div class="project-footer" aria-label="Technologies used">
                    {stack_html}
                </div>
            </article>"""
        project_cards.append(card_html)
    projects_html = "\n\n".join(project_cards)

    # Render Learning Cards
    learning_cards = []
    for item in learning:
        card_html = f"""            <article class="learning-card">
                <span class="learning-status-pill">{item['status']}</span>
                <h3 class="learning-topic">{item['topic']}</h3>
                <div class="learning-focus">{item['focus']}</div>
                <p class="learning-description">{item['description']}</p>
            </article>"""
        learning_cards.append(card_html)
    learning_html = "\n\n".join(learning_cards)

    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{profile['name']} — Portfolio | CSE &amp; Cybersecurity</title>
    
    <!-- Meta & SEO Tags -->
    <meta name="description" content="{profile['name']} — {profile['headline']} Hands-on projects in Python, C, networking fundamentals, and data structures.">
    <meta name="author" content="{profile['name']}">
    <meta name="theme-color" content="#090a0f">

    <!-- Open Graph / Social Media -->
    <meta property="og:type" content="website">
    <meta property="og:title" content="{profile['name']} — Personal Portfolio">
    <meta property="og:description" content="{profile['headline']}">
    <meta property="og:url" content="https://mayank-portfolio.vercel.app/">
    
    <!-- Favicon (Clean SVG monogram) -->
    <link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><rect width='100' height='100' rx='20' fill='%2311131a'/><text x='50' y='65' font-family='sans-serif' font-size='48' font-weight='700' fill='%2338bdf8' text-anchor='middle'>MR</text></svg>">

    <!-- Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:ital,wght@0,400;0,500;0,600;0,700;1,400&family=Space+Grotesk:wght@500;600;700&family=JetBrains+Mono:wght@400;500;600&display=swap" rel="stylesheet">

    <!-- Stylesheet -->
    <link rel="stylesheet" href="css/style.css?v=2.1">
</head>
<body>
    <!-- Accessibility: Skip Link -->
    <a href="#main-content" class="skip-link">Skip to main content</a>

    <!-- Site Header & Navigation -->
    <header class="site-header">
        <div class="header-inner">
            <a href="#hero" class="brand-link" aria-label="{profile['name']} - Home">
                <span class="brand-mark">MR</span>
                <span class="brand-name">{profile['name']}</span>
            </a>

            <!-- Mobile Nav Toggle -->
            <button class="mobile-nav-toggle" aria-expanded="false" aria-controls="nav-links" aria-label="Toggle navigation menu">
                <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
                    <line x1="3" y1="12" x2="21" y2="12"></line>
                    <line x1="3" y1="6" x2="21" y2="6"></line>
                    <line x1="3" y1="18" x2="21" y2="18"></line>
                </svg>
            </button>

            <!-- Navigation Links -->
            <nav aria-label="Primary navigation">
                <ul class="nav-links" id="nav-links">
                    <li><a href="#about" class="nav-link">About</a></li>
                    <li><a href="#skills" class="nav-link">Skills &amp; Focus</a></li>
                    <li><a href="#projects" class="nav-link">Projects</a></li>
                    <li><a href="#learning" class="nav-link">Current Learning</a></li>
                    <li><a href="#contact" class="nav-link">Contact</a></li>
                </ul>
            </nav>
        </div>
    </header>

    <!-- Main Content -->
    <main id="main-content" class="page-container page-wrapper">
        
        <!-- 1. Hero Section -->
        <section class="section hero-section" id="hero" aria-label="Introduction">
            <div class="hero-greeting">
                <span>✦</span>
                <span>Computer Science Engineering Student</span>
            </div>
            <h1 class="hero-name">Hi, I'm {profile['name']}.</h1>
            <p class="hero-headline">{profile['headline']}</p>
            <p class="hero-bio">{profile['bio']}</p>

            <div class="hero-actions">
                <a href="#projects" class="btn btn-primary">
                    <span>View projects</span>
                    <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m6 9 6 6 6-6"/></svg>
                </a>
                <a href="#contact" class="btn btn-secondary">
                    <span>Contact me</span>
                </a>
            </div>

            <div class="hero-socials" aria-label="Direct profiles and contact">
                <span class="hero-socials-label">Connect:</span>
                <a href="mailto:{profile['email']}" class="social-pill" aria-label="Email {profile['name']}">
                    {ICONS['email']}
                    <span>Email</span>
                </a>
                <a href="{profile['github']}" target="_blank" rel="noopener noreferrer" class="social-pill" aria-label="GitHub profile (opens in new tab)">
                    {ICONS['github']}
                    <span>GitHub</span>
                    {ICONS['external']}
                </a>
                <a href="{profile['linkedin']}" target="_blank" rel="noopener noreferrer" class="social-pill" aria-label="LinkedIn profile (opens in new tab)">
                    {ICONS['linkedin']}
                    <span>LinkedIn</span>
                    {ICONS['external']}
                </a>
                <a href="{profile['discord']}" target="_blank" rel="noopener noreferrer" class="social-pill" aria-label="Discord contact (opens in new tab)">
                    {ICONS['discord']}
                    <span>Discord</span>
                    {ICONS['external']}
                </a>
                <a href="{profile['instagram']}" target="_blank" rel="noopener noreferrer" class="social-pill" aria-label="Instagram profile (opens in new tab)">
                    {ICONS['instagram']}
                    <span>Instagram</span>
                    {ICONS['external']}
                </a>
            </div>
        </section>

        <!-- 2. About Section -->
        <section class="section about-section" id="about" aria-labelledby="about-title">
            <div class="section-header">
                <div class="section-label">Background</div>
                <h2 id="about-title" class="section-title">About Me</h2>
            </div>

            <div class="about-grid">
                <div class="about-content">
                    <p>I am a first-year Computer Science Engineering student actively exploring cybersecurity and systems programming.</p>
                    <p>{profile['about']}</p>
                </div>
                <aside class="about-sidebar" aria-label="Quick overview">
                    <dl class="about-meta-list">
                        <div class="about-meta-item">
                            <dt>Status</dt>
                            <dd>1st Year CSE Student</dd>
                        </div>
                        <div class="about-meta-item">
                            <dt>Primary Interest</dt>
                            <dd>Cybersecurity &amp; Systems</dd>
                        </div>
                        <div class="about-meta-item">
                            <dt>Core Stack</dt>
                            <dd>Python, C, TypeScript</dd>
                        </div>
                        <div class="about-meta-item">
                            <dt>Learning Focus</dt>
                            <dd>Networking &amp; DSA</dd>
                        </div>
                    </dl>
                </aside>
            </div>
        </section>

        <!-- 3. Skills and Current Focus Section -->
        <section class="section skills-section" id="skills" aria-labelledby="skills-title">
            <div class="section-header">
                <div class="section-label">Capabilities</div>
                <h2 id="skills-title" class="section-title">Skills &amp; Technical Focus</h2>
                <p class="section-description">A clear breakdown of tools I use for building projects alongside areas of ongoing academic and self-directed study.</p>
            </div>

            <div class="skills-grid">
                <!-- Group 1: Programming -->
                <div class="skill-category-card">
                    <div class="skill-category-header">
                        <h3 class="skill-category-title">Programming</h3>
                        <p class="skill-category-caption">Core languages used for coursework, scripting, and hands-on exercises.</p>
                    </div>
                    <ul class="skill-list">
{prog_skills}
                    </ul>
                </div>

                <!-- Group 2: Web & Tools -->
                <div class="skill-category-card">
                    <div class="skill-category-header">
                        <h3 class="skill-category-title">Web &amp; Development Tools</h3>
                        <p class="skill-category-caption">Technologies applied in project interfaces and version control.</p>
                    </div>
                    <ul class="skill-list">
{web_skills}
                    </ul>
                </div>

                <!-- Group 3: Current Exploration -->
                <div class="skill-category-card">
                    <div class="skill-category-header">
                        <h3 class="skill-category-title">Current Focus (Learning)</h3>
                        <p class="skill-category-caption">Foundational engineering concepts under active study.</p>
                    </div>
                    <ul class="skill-list">
{learn_skills}
                    </ul>
                </div>
            </div>
        </section>

        <!-- 4. Projects Section -->
        <section class="section projects-section" id="projects" aria-labelledby="projects-title">
            <div class="section-header">
                <div class="section-label">Portfolio</div>
                <h2 id="projects-title" class="section-title">Projects</h2>
                <p class="section-description">Functional prototypes and applications built to solve real-world tasks and reinforce programming concepts.</p>
            </div>

            <div class="projects-grid project-grid">
{projects_html}
            </div>
        </section>

        <!-- 5. Current Learning / Updates Section -->
        <section class="section learning-section" id="learning" aria-labelledby="learning-title">
            <div class="section-header">
                <div class="section-label">Active Exploration</div>
                <h2 id="learning-title" class="section-title">Current Learning</h2>
                <p class="section-description">Specific topics under regular study, focused on building core engineering principles without artificial milestones.</p>
            </div>

            <div class="learning-grid">
{learning_html}
            </div>
        </section>

        <!-- 6. Contact Section -->
        <section class="section contact-section" id="contact" aria-labelledby="contact-title">
            <div class="contact-wrapper">
                <div class="section-header">
                    <div class="section-label">Communication</div>
                    <h2 id="contact-title" class="section-title">Get in Touch</h2>
                </div>

                <div class="contact-layout">
                    <div>
                        <p class="contact-pitch">
                            I am always open to feedback on my projects, learning recommendations, and conversations regarding early-career cybersecurity opportunities and student collaborations.
                        </p>
                        <div class="contact-actions">
                            <a href="mailto:{profile['email']}" class="btn btn-primary">
                                {ICONS['email']}
                                <span>Send an email</span>
                            </a>
                            <button type="button" class="btn btn-secondary" id="copy-email-btn" aria-label="Copy email address to clipboard">
                                {ICONS['copy']}
                                <span>Copy email address</span>
                            </button>
                        </div>
                        <div class="copy-status-message" id="copy-status" role="status" aria-live="polite"></div>
                    </div>

                    <div class="contact-links-sidebar" aria-label="Profiles and external links">
                        <a href="{profile['github']}" target="_blank" rel="noopener noreferrer" class="contact-link-row" aria-label="GitHub profile of {profile['name']} (opens in new tab)">
                            <div class="contact-link-info">
                                {ICONS['github']}
                                <span>GitHub</span>
                            </div>
                            <span class="contact-link-badge">Mayank-Rathi-create ↗</span>
                        </a>

                        <a href="{profile['linkedin']}" target="_blank" rel="noopener noreferrer" class="contact-link-row" aria-label="LinkedIn profile of {profile['name']} (opens in new tab)">
                            <div class="contact-link-info">
                                {ICONS['linkedin']}
                                <span>LinkedIn</span>
                            </div>
                            <span class="contact-link-badge">Connect ↗</span>
                        </a>

                        <a href="{profile['discord']}" target="_blank" rel="noopener noreferrer" class="contact-link-row" aria-label="Discord handle of {profile['name']} (opens in new tab)">
                            <div class="contact-link-info">
                                {ICONS['discord']}
                                <span>Discord</span>
                            </div>
                            <span class="contact-link-badge">@{profile.get('discord_handle', 'mayankrathi0719')} ↗</span>
                        </a>

                        <a href="{profile['instagram']}" target="_blank" rel="noopener noreferrer" class="contact-link-row" aria-label="Instagram profile of {profile['name']} (opens in new tab)">
                            <div class="contact-link-info">
                                {ICONS['instagram']}
                                <span>Instagram</span>
                            </div>
                            <span class="contact-link-badge">@mayank_rathi11 ↗</span>
                        </a>
                    </div>
                </div>
            </div>
        </section>

    </main>

    <!-- Site Footer -->
    <footer class="site-footer">
        <div class="footer-inner">
            <div class="footer-credits">
                © <span id="year">2026</span> {profile['name']} · Built with semantic HTML &amp; CSS
            </div>
            <a href="#hero" class="footer-back-to-top" aria-label="Back to top of page">↑ Back to top</a>
        </div>
    </footer>

    <!-- Client Script -->
    <script src="js/main.js?v=2.1" defer></script>
</body>
</html>
"""

    with open(HTML_FILE, "w", encoding="utf-8") as f:
        f.write(html_content)

    print("✅ index.html generated successfully from data/portfolio.json!")


if __name__ == "__main__":
    build()
