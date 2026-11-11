/**
 * Mayank Rathi — Portfolio
 * Lightweight client interactions & subtle interactive enhancements
 */

document.addEventListener('DOMContentLoaded', () => {
    // 1. Dynamic Year in Footer
    const yearElement = document.getElementById('year');
    if (yearElement) {
        yearElement.textContent = new Date().getFullYear();
    }

    // 2. Interactive Card Spotlight / Glow on mouse movement
    const cards = document.querySelectorAll('.project-card, .chronicle-item, .contact-card');
    
    // Check if user prefers reduced motion
    const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    
    if (!prefersReducedMotion) {
        cards.forEach(card => {
            card.addEventListener('mousemove', (e) => {
                const rect = card.getBoundingClientRect();
                const x = e.clientX - rect.left;
                const y = e.clientY - rect.top;
                
                card.style.setProperty('--mouse-x', `${x}px`);
                card.style.setProperty('--mouse-y', `${y}px`);
            });
        });
    }

    // 3. Console Easter Egg for Cybersecurity / CSE peers
    console.log(
        '%c✦ Mayank Rathi %c| CSE & Cybersecurity Explorer',
        'color: #38bdf8; font-weight: bold; font-size: 14px;',
        'color: #94a3b8; font-size: 13px;'
    );
    console.log(
        '%cInterested in collaborating or checking out systems code? Reach out via email or GitHub!',
        'color: #64748b; font-size: 11px;'
    );
});

