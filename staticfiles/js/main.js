document.addEventListener('DOMContentLoaded', () => {
    console.log('Main.js loaded');

    // Mobile Menu Toggle
    const mobileMenuBtn = document.querySelector('.mobile-menu-btn');
    const navLinks = document.querySelector('.nav-links');
    
    if (mobileMenuBtn && navLinks) {
        mobileMenuBtn.addEventListener('click', () => {
            navLinks.classList.toggle('active');
            
            // Toggle icon between bars and times
            const icon = mobileMenuBtn.querySelector('i');
            if (icon) {
                if (navLinks.classList.contains('active')) {
                    icon.classList.remove('fa-bars');
                    icon.classList.add('fa-times');
                } else {
                    icon.classList.remove('fa-times');
                    icon.classList.add('fa-bars');
                }
            }
        });
    }

    // Add to Cart Logic
    const addToCartBtn = document.querySelector('.btn-primary');
    if (addToCartBtn && addToCartBtn.textContent.includes('Ajouter au Panier')) {
        addToCartBtn.addEventListener('click', (e) => {
            e.preventDefault();
            
            // Get product info from page (basic implementation)
            const productTitle = document.querySelector('h1')?.textContent;
            const quantity = document.querySelector('input[type="number"]')?.value || 1;

            // Show feedback
            const originalText = addToCartBtn.innerHTML;
            addToCartBtn.innerHTML = '<i class="fas fa-check"></i> Ajouté !';
            addToCartBtn.style.background = '#059669'; // Darker green

            // Reset after 2 seconds
            setTimeout(() => {
                addToCartBtn.innerHTML = originalText;
                addToCartBtn.style.background = '';
            }, 2000);

            // Optional: Save to localStorage for a simple cart
            let cart = JSON.parse(localStorage.getItem('cart') || '[]');
            cart.push({ title: productTitle, quantity: quantity, date: new Date().toISOString() });
            localStorage.setItem('cart', JSON.stringify(cart));
            
            updateCartCount();
            console.log('Product added to cart:', productTitle, 'Qty:', quantity);
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

    // Initial load
    updateCartCount();
});
