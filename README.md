# Mayank Rathhi — Portfolio

A calm, technical, high-performance personal portfolio website built with semantic HTML5, modern CSS, and clean accessibility practices. Designed for zero-config edge deployment on **Vercel** with a companion **Python / Streamlit** mode.

---

## 🚀 How to Deploy on Vercel

This repository is optimized for Vercel out of the box with zero build setup required:

### Option 1: Deploy via GitHub (Recommended)
1. Push your repository to **GitHub**:
   ```bash
   git add .
   git commit -m "Enhance portfolio structure and accessibility"
   git push origin main
   ```
2. Go to [vercel.com](https://vercel.com) and log in.
3. Click **"Add New..."** > **"Project"**.
4. Select your **`Mayank-portfolio`** repository.
5. In project settings:
   - **Framework Preset**: *Other* (auto-detected Static Site)
   - **Root Directory**: `./`
   - **Build Command**: *Leave empty*
   - **Output Directory**: *Leave empty*
6. Click **Deploy**. Your site will be live globally in seconds!

### Option 2: Deploy using Vercel CLI
```bash
npm i -g vercel
vercel --prod
```

---

## 📁 Project Structure

```
Mayank-portfolio/
├── index.html            # Production entry point for Vercel (semantic HTML5, SEO & a11y)
├── vercel.json           # Vercel deployment headers and routing configuration
├── build.py              # Generator script to sync data/portfolio.json into index.html
├── portfolio.py          # Python/Streamlit version (reads from data/ and css/)
├── requirements.txt      # Python dependencies (Streamlit)
├── .gitignore            # Git ignore rules for Python, cache, and Vercel
│
├── data/
│   └── portfolio.json    # Centralized data source for profile, skills, projects, and learning
│
├── css/
│   └── style.css         # High-contrast, responsive dark theme design system
│
└── js/
    └── main.js           # Accessible mobile menu, clipboard email copy & dynamic year
```

---

## 🛠️ How to Customize Your Content

All personal content is neatly organized in **`data/portfolio.json`**:
- **`profile`**: Name, headline, bio, about, email, and social profiles.
- **`skills`**: Categorized into Programming, Web & Tools, and Current Focus.
- **`projects`**: Project titles, descriptions, demonstrated skills, stack tags, and URLs.
- **`learning_dispatches`**: Ongoing learning topics, active status, and focus descriptions.

### Regenerate `index.html` after modifying `portfolio.json`:
```bash
python build.py
```

---

## 💻 Running Locally

### Option A: Static Web (Instant)
- **VS Code**: Install *Live Server* extension and click "Go Live" on `index.html`.
- **Python Built-in Server**:
  ```bash
  python -m http.server 3000
  ```
  Then visit `http://localhost:3000`.

### Option B: Streamlit Application
```bash
pip install -r requirements.txt
streamlit run portfolio.py
```

---

## 🛡️ Author
**Mayank Rathhi** — First-year Computer Science Engineering student exploring cybersecurity.
