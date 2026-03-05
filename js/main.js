// main.js — Purava Website

document.addEventListener('DOMContentLoaded', () => {

    // ---- Transparent / Solid Header on Scroll (index.html only) ----
    const header = document.getElementById('site-header');
    if (header && header.classList.contains('transparent')) {
        window.addEventListener('scroll', () => {
            if (window.scrollY > 60) {
                header.classList.replace('transparent', 'solid');
            } else {
                header.classList.replace('solid', 'transparent');
            }
        });
    }

    // ---- Mobile Menu Toggle ----
    const menuBtn = document.getElementById('menuToggle');
    const navLinks = document.getElementById('navLinks');
    if (menuBtn && navLinks) {
        menuBtn.addEventListener('click', () => {
            navLinks.classList.toggle('open');
            const icon = menuBtn.querySelector('i');
            if (navLinks.classList.contains('open')) {
                icon.className = 'ph ph-x';
            } else {
                icon.className = 'ph ph-list';
            }
        });
    }

    // ---- Scroll Reveal Animations ----
    const revealEls = document.querySelectorAll('.reveal-up, .reveal');
    if (revealEls.length > 0) {
        const revealObs = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('active');
                    revealObs.unobserve(entry.target);
                }
            });
        }, { threshold: 0.12, rootMargin: '0px 0px -40px 0px' });
        revealEls.forEach(el => revealObs.observe(el));
    }

    // ---- FAQ Accordion ----
    const faqItems = document.querySelectorAll('.faq-item');
    faqItems.forEach(item => {
        const question = item.querySelector('.faq-question');
        if (question) {
            question.addEventListener('click', () => {
                const isOpen = item.classList.contains('active');
                faqItems.forEach(fi => fi.classList.remove('active'));
                if (!isOpen) item.classList.add('active');
            });
        }
    });

    // ---- Smooth Anchor Scroll ----
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            const targetId = this.getAttribute('href');
            if (targetId === '#') return;
            const target = document.querySelector(targetId);
            if (target) {
                e.preventDefault();
                if (navLinks) navLinks.classList.remove('open');
                target.scrollIntoView({ behavior: 'smooth', block: 'start' });
            }
        });
    });

    // ---- Product filter chips (visual only) ----
    const chips = document.querySelectorAll('.filter-chip');
    chips.forEach(chip => {
        chip.addEventListener('click', () => {
            chips.forEach(c => c.classList.remove('active'));
            chip.classList.add('active');
        });
    });

});
