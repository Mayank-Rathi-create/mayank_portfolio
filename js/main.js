/**
 * Mayank Rathhi — Personal Portfolio
 * Accessible client interactions: navigation toggle, clipboard utility, dynamic year
 */

document.addEventListener('DOMContentLoaded', () => {
    // 1. Dynamic Year in Footer
    const yearEl = document.getElementById('year');
    if (yearEl) {
        yearEl.textContent = new Date().getFullYear();
    }

    // 2. Mobile Navigation Toggle
    const navToggle = document.querySelector('.mobile-nav-toggle');
    const navLinks = document.getElementById('nav-links');

    if (navToggle && navLinks) {
        const toggleNav = () => {
            const isExpanded = navToggle.getAttribute('aria-expanded') === 'true';
            navToggle.setAttribute('aria-expanded', String(!isExpanded));
            navLinks.classList.toggle('is-open', !isExpanded);
        };

        navToggle.addEventListener('click', toggleNav);

        // Close menu when clicking any nav link
        navLinks.querySelectorAll('.nav-link').forEach(link => {
            link.addEventListener('click', () => {
                if (navLinks.classList.contains('is-open')) {
                    navToggle.setAttribute('aria-expanded', 'false');
                    navLinks.classList.remove('is-open');
                }
            });
        });

        // Close on ESC key press
        document.addEventListener('keydown', (e) => {
            if (e.key === 'Escape' && navLinks.classList.contains('is-open')) {
                navToggle.setAttribute('aria-expanded', 'false');
                navLinks.classList.remove('is-open');
                navToggle.focus();
            }
        });
    }

    // 3. Accessible Email Copy Helper
    const copyBtn = document.getElementById('copy-email-btn');
    const statusMsg = document.getElementById('copy-status');
    const emailToCopy = 'mayankrathinp@gmail.com';

    if (copyBtn && statusMsg) {
        copyBtn.addEventListener('click', async () => {
            try {
                if (navigator.clipboard && navigator.clipboard.writeText) {
                    await navigator.clipboard.writeText(emailToCopy);
                    statusMsg.textContent = 'Email address copied to clipboard.';
                } else {
                    // Fallback
                    const textArea = document.createElement('textarea');
                    textArea.value = emailToCopy;
                    textArea.style.position = 'fixed';
                    textArea.style.left = '-999999px';
                    document.body.appendChild(textArea);
                    textArea.select();
                    document.execCommand('copy');
                    document.body.removeChild(textArea);
                    statusMsg.textContent = 'Email address copied to clipboard.';
                }

                setTimeout(() => {
                    statusMsg.textContent = '';
                }, 3000);
            } catch (err) {
                statusMsg.textContent = `Email: ${emailToCopy}`;
            }
        });
    }
});
