document.addEventListener('DOMContentLoaded', () => {
    console.log('Main.js loaded');

    // ── MOBILE MENU TOGGLE ──────────────────────────────────────────
    const mobileMenuBtn = document.querySelector('.mobile-menu-btn');
    const navLinks = document.querySelector('.nav-links');
    const navbar = document.querySelector('.navbar');

    if (mobileMenuBtn && navLinks) {
        mobileMenuBtn.addEventListener('click', (e) => {
            e.stopPropagation();
            navLinks.classList.toggle('active');

            const icon = mobileMenuBtn.querySelector('i');
            if (icon) {
                if (navLinks.classList.contains('active')) {
                    icon.classList.remove('fa-bars');
                    icon.classList.add('fa-times');
                } else {
                    icon.classList.remove('fa-times');
                    icon.classList.add('fa-bars');
                    // Close all mega menus when closing nav
                    document.querySelectorAll('.mega-menu').forEach(m => m.classList.remove('mobile-open'));
                }
            }
        });

        // Close drawer when clicking outside
        document.addEventListener('click', (e) => {
            if (navLinks.classList.contains('active') &&
                !navLinks.contains(e.target) &&
                !mobileMenuBtn.contains(e.target)) {
                navLinks.classList.remove('active');
                const icon = mobileMenuBtn.querySelector('i');
                if (icon) {
                    icon.classList.remove('fa-times');
                    icon.classList.add('fa-bars');
                }
            }
        });
    }

    // ── MOBILE MEGA MENU TOGGLE ─────────────────────────────────────
    const isMobile = () => window.innerWidth <= 768;

    document.querySelectorAll('.has-mega > a').forEach(link => {
        link.addEventListener('click', (e) => {
            if (isMobile()) {
                e.preventDefault();
                const megaMenu = link.nextElementSibling;
                if (megaMenu && megaMenu.classList.contains('mega-menu')) {
                    megaMenu.classList.toggle('mobile-open');
                    // Toggle arrow icon
                    const chevron = link.querySelector('.fa-chevron-down');
                    if (chevron) {
                        chevron.style.transform = megaMenu.classList.contains('mobile-open')
                            ? 'rotate(180deg)' : 'rotate(0)';
                        chevron.style.transition = 'transform 0.3s';
                    }
                }
            }
        });
    });

    // ── ADD TO CART ─────────────────────────────────────────────────
    const addToCartBtn = document.querySelector('.btn-primary');
    if (addToCartBtn && addToCartBtn.textContent.includes('Ajouter au Panier')) {
        addToCartBtn.addEventListener('click', (e) => {
            e.preventDefault();
            const productTitle = document.querySelector('h1')?.textContent;
            const quantity = document.querySelector('input[type="number"]')?.value || 1;

            const originalText = addToCartBtn.innerHTML;
            addToCartBtn.innerHTML = '<i class="fas fa-check"></i> Ajouté !';
            addToCartBtn.style.background = '#059669';

            setTimeout(() => {
                addToCartBtn.innerHTML = originalText;
                addToCartBtn.style.background = '';
            }, 2000);

            let cart = JSON.parse(localStorage.getItem('cart') || '[]');
            cart.push({ title: productTitle, quantity: quantity, date: new Date().toISOString() });
            localStorage.setItem('cart', JSON.stringify(cart));

            updateCartCount();
        });
    }

    function updateCartCount() {
        const cart = JSON.parse(localStorage.getItem('cart') || '[]');
        const countBadge = document.getElementById('cart-count');
        if (countBadge) {
            if (cart.length > 0) {
                countBadge.textContent = cart.length;
                countBadge.style.display = 'inline-block';
            } else {
                countBadge.style.display = 'none';
            }
        }
    }

    updateCartCount();
});
