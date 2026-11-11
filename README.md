# Mayank Rathi — Portfolio

A minimalist, high-performance portfolio website built with clean web standards and designed for zero-config, instant deployment on **Vercel** (as well as Python/Streamlit environments).

---

## 🚀 How to Deploy on Vercel

This repository is optimized for Vercel out of the box with zero build setup required:

### Option 1: Deploy via GitHub (Recommended)
1. Push your repository to **GitHub**:
   ```bash
   git add .
   git commit -m "Organize code for Vercel deployment"
   git push origin main
   ```
2. Go to [vercel.com](https://vercel.com) and log in.
3. Click **"Add New..."** > **"Project"**.
4. Select your **`Mayank-portfolio`** repository.
5. In the project settings:
   - **Framework Preset**: *Other* (or auto-detected Static Site)
   - **Root Directory**: `./`
   - **Build Command**: *Leave empty*
   - **Output Directory**: *Leave empty*
6. Click **Deploy**. Your portfolio will be live worldwide in seconds!

### Option 2: Deploy using Vercel CLI
If you have Node.js / Vercel CLI installed:
```bash
npm i -g vercel
vercel
```
Follow the quick CLI prompts to deploy. For production deployment, run:
```bash
vercel --prod
```

---

## 📁 Project Structure

```
Mayank-portfolio/
├── index.html            # Production entry point for Vercel (semantic HTML & SEO)
├── vercel.json           # Vercel deployment headers and routing configuration
├── build.py              # Generator script to sync data/portfolio.json into index.html
├── portfolio.py          # Python/Streamlit application (reads from data/ & css/)
├── requirements.txt      # Python dependencies (Streamlit)
├── .gitignore            # Git ignore rules for Python, cache, and Vercel
│
├── data/
│   └── portfolio.json    # Single source of truth for bio, skills, projects, and blogs
│
├── css/
│   └── style.css         # Minimalist design system, typography, animations & dark theme
│
└── js/
    └── main.js           # Client interactions (dynamic year, subtle hover effects)
```

---

## 🛠️ How to Customize Your Content

All personal content (profile information, projects, and learning updates) is neatly organized in **`data/portfolio.json`**.

### 1. Edit your content
Open `data/portfolio.json` and update:
- **`profile`**: Name, bio, email, social links, focus areas.
- **`projects`**: Add or modify projects (title, description, tech stack, URL).
- **`blogs`**: Add or modify learning field notes and articles.

### 2. Update the website
After editing `data/portfolio.json`, update `index.html` by running:
```bash
python build.py
```
*(You can also edit `index.html` directly if you prefer HTML).*

---

## 💻 Running Locally

### Option A: Static Web (Instant)
- **VS Code**: Install the *Live Server* extension and click "Go Live" on `index.html`.
- **Python Built-in Server**:
  ```bash
  python -m http.server 3000
  ```
  Then open `http://localhost:3000` in your browser.

### Option B: Streamlit App
If you wish to run the app using Streamlit:
```bash
pip install -r requirements.txt
streamlit run portfolio.py
```

---

## 🛡️ License & Author
Created by **Mayank Rathi** — CSE student building toward a career in cybersecurity.
