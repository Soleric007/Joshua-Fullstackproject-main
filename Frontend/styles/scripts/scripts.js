// Simple timer for flash sales
function updateTimer() {
    const timerBoxes = document.querySelectorAll('.timer-box');
    if (timerBoxes.length === 0) return;
    
    let time = [2, 45, 18]; // hours, minutes, seconds
    
    setInterval(() => {
        time[2]--;
        
        if (time[2] < 0) {
            time[2] = 59;
            time[1]--;
        }
        
        if (time[1] < 0) {
            time[1] = 59;
            time[0]--;
        }
        
        if (time[0] < 0) {
            time = [2, 45, 18]; // Reset timer
        }
        
        // Format time to always show two digits
        const formattedTime = time.map(unit => unit.toString().padStart(2, '0'));
        
        timerBoxes.forEach((box, index) => {
            box.textContent = formattedTime[index];
        });
    }, 1000);
}

// Add to cart functionality
function setupAddToCart() {
    document.querySelectorAll('.add-to-cart').forEach(button => {
        button.addEventListener('click', function(e) {
            e.stopPropagation(); // Prevent triggering product card click
            const productTitle = this.closest('.product-card').querySelector('.product-title').textContent;
            alert(`${productTitle} added to cart!`);
            
            // Update cart count in header
            updateCartCount();
        });
    });
}

// Update cart count in header
function updateCartCount() {
    const cartElement = document.querySelector('.user-actions a:nth-child(3) span');
    if (cartElement) {
        const currentCount = parseInt(cartElement.textContent.match(/\d+/) || 0);
        cartElement.textContent = `Cart (${currentCount + 1})`;
    }
}

// Search functionality
function setupSearch() {
    const searchInput = document.querySelector('.search-bar input');
    const searchButton = document.querySelector('.search-bar button');
    
    if (!searchInput || !searchButton) return;
    
    const performSearch = () => {
        const searchTerm = searchInput.value.trim();
        if (searchTerm) {
            alert(`Searching for: ${searchTerm}`);
            // In a real application, you would redirect to search results page
            // or filter products based on search term
        }
    };
    
    searchButton.addEventListener('click', performSearch);
    searchInput.addEventListener('keypress', (e) => {
        if (e.key === 'Enter') {
            performSearch();
        }
    });
}

// Category page functionality
function setupCategoryPages() {
    // Filter functionality
    const applyFiltersBtn = document.querySelector('.apply-filters');
    if (applyFiltersBtn) {
        applyFiltersBtn.addEventListener('click', function() {
            alert('Filters applied!');
            // In a real application, this would filter the products
        });
    }

    // Sort functionality
    const sortSelect = document.querySelector('.sort-options select');
    if (sortSelect) {
        sortSelect.addEventListener('change', function() {
            alert(`Sorted by: ${this.value}`);
            // In a real application, this would sort the products
        });
    }

    // Pagination
    const pageLinks = document.querySelectorAll('.page-link');
    pageLinks.forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            if (!this.classList.contains('active')) {
                document.querySelector('.page-link.active')?.classList.remove('active');
                this.classList.add('active');
                alert(`Navigating to page ${this.textContent}`);
                // In a real application, this would load the corresponding page
            }
        });
    });
}

// Enhanced category navigation
function setupCategoryNavigation() {
    document.querySelectorAll('.category-card').forEach(card => {
        card.addEventListener('click', function() {
            const categoryName = this.querySelector('h3').textContent.toLowerCase();
            
            if (categoryName.includes('phone') || categoryName.includes('tablet')) {
                window.location.href = 'phones.html';
            } else if (categoryName.includes('comput') || categoryName.includes('laptop')) {
                window.location.href = 'computers.html';
            } else if (categoryName.includes('electron') || categoryName.includes('tv')) {
                window.location.href = 'electronics.html';
            } else if (categoryName.includes('home') || categoryName.includes('kitchen')) {
                window.location.href = 'home-kitchen.html';
            } else if (categoryName.includes('fashion') || categoryName.includes('cloth')) {
                window.location.href = 'fashion.html';
            } else if (categoryName.includes('health') || categoryName.includes('beauty')) {
                window.location.href = 'health-beauty.html';
            } else if (categoryName.includes('game')) {
                window.location.href = 'electronics.html'; // Gaming under electronics
            } else if (categoryName.includes('baby')) {
                window.location.href = 'home-kitchen.html'; // Baby products under home
            }
        });
    });
}

// Product card click navigation (for product details)
function setupProductNavigation() {
    document.querySelectorAll('.product-card').forEach(card => {
        card.addEventListener('click', function(e) {
            // Only navigate if the click wasn't on the add-to-cart button
            if (!e.target.closest('.add-to-cart')) {
                const productTitle = this.querySelector('.product-title').textContent;
                alert(`Navigating to ${productTitle} details page`);
                // In a real application, this would navigate to product detail page
            }
        });
    });
}

// Mobile menu functionality
function setupMobileMenu() {
    const mobileMenuBtn = document.createElement('button');
    mobileMenuBtn.innerHTML = '<i class="fas fa-bars"></i>';
    mobileMenuBtn.className = 'mobile-menu-btn';
    
    const headerBottom = document.querySelector('.header-bottom');
    if (headerBottom && window.innerWidth <= 768) {
        headerBottom.parentNode.insertBefore(mobileMenuBtn, headerBottom);
        
        mobileMenuBtn.addEventListener('click', function() {
            headerBottom.classList.toggle('active');
        });
    }
}

// Smooth scrolling for anchor links
function setupSmoothScrolling() {
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });
}

// Initialize all functionality when DOM is loaded
document.addEventListener('DOMContentLoaded', function() {
    updateTimer();
    setupAddToCart();
    setupSearch();
    setupCategoryPages();
    setupCategoryNavigation();
    setupProductNavigation();
    setupMobileMenu();
    setupSmoothScrolling();
    
    // Add hover effects to category cards
    document.querySelectorAll('.category-card').forEach(card => {
        card.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-5px)';
        });
        
        card.addEventListener('mouseleave', function() {
            this.style.transform = 'translateY(0)';
        });
    });
    
    // Add loading animation to product cards
    document.querySelectorAll('.product-card').forEach(card => {
        card.style.opacity = '0';
        card.style.transform = 'translateY(20px)';
        card.style.transition = 'all 0.5s ease';
        
        setTimeout(() => {
            card.style.opacity = '1';
            card.style.transform = 'translateY(0)';
        }, 100);
    });
});

// Additional utility functions
const utils = {
    // Format price with currency
    formatPrice: (price) => {
        return new Intl.NumberFormat('en-US', {
            style: 'currency',
            currency: 'USD'
        }).format(price);
    },
    
    // Generate star rating HTML
    generateStarRating: (rating) => {
        const fullStars = Math.floor(rating);
        const hasHalfStar = rating % 1 !== 0;
        let starsHTML = '';
        
        for (let i = 0; i < fullStars; i++) {
            starsHTML += '<i class="fas fa-star"></i>';
        }
        
        if (hasHalfStar) {
            starsHTML += '<i class="fas fa-star-half-alt"></i>';
        }
        
        const emptyStars = 5 - Math.ceil(rating);
        for (let i = 0; i < emptyStars; i++) {
            starsHTML += '<i class="far fa-star"></i>';
        }
        
        return starsHTML;
    },
    
    // Debounce function for search
    debounce: (func, wait) => {
        let timeout;
        return function executedFunction(...args) {
            const later = () => {
                clearTimeout(timeout);
                func(...args);
            };
            clearTimeout(timeout);
            timeout = setTimeout(later, wait);
        };
    },
    
    // Format date
    formatDate: (date) => {
        return new Date(date).toLocaleDateString('en-US', {
            year: 'numeric',
            month: 'long',
            day: 'numeric'
        });
    },
    
    // Validate email
    validateEmail: (email) => {
        const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        return re.test(email);
    }
};

// Cart management functionality
const cartManager = {
    items: [],
    
    addItem: function(product) {
        const existingItem = this.items.find(item => item.id === product.id);
        if (existingItem) {
            existingItem.quantity += 1;
        } else {
            this.items.push({
                ...product,
                quantity: 1
            });
        }
        this.saveToLocalStorage();
        this.updateCartUI();
    },
    
    removeItem: function(productId) {
        this.items = this.items.filter(item => item.id !== productId);
        this.saveToLocalStorage();
        this.updateCartUI();
    },
    
    updateQuantity: function(productId, quantity) {
        const item = this.items.find(item => item.id === productId);
        if (item) {
            item.quantity = quantity;
            if (item.quantity <= 0) {
                this.removeItem(productId);
            }
        }
        this.saveToLocalStorage();
        this.updateCartUI();
    },
    
    getTotal: function() {
        return this.items.reduce((total, item) => total + (item.price * item.quantity), 0);
    },
    
    getItemCount: function() {
        return this.items.reduce((count, item) => count + item.quantity, 0);
    },
    
    saveToLocalStorage: function() {
        localStorage.setItem('shopnow-cart', JSON.stringify(this.items));
    },
    
    loadFromLocalStorage: function() {
        const savedCart = localStorage.getItem('shopnow-cart');
        if (savedCart) {
            this.items = JSON.parse(savedCart);
            this.updateCartUI();
        }
    },
    
    updateCartUI: function() {
        const cartCount = this.getItemCount();
        const cartElement = document.querySelector('.user-actions a:nth-child(3) span');
        if (cartElement) {
            cartElement.textContent = `Cart (${cartCount})`;
        }
    },
    
    clearCart: function() {
        this.items = [];
        this.saveToLocalStorage();
        this.updateCartUI();
    }
};

// Initialize cart manager when DOM is loaded
document.addEventListener('DOMContentLoaded', function() {
    cartManager.loadFromLocalStorage();
});

// Wishlist functionality
const wishlistManager = {
    items: [],
    
    addItem: function(product) {
        if (!this.items.find(item => item.id === product.id)) {
            this.items.push(product);
            this.saveToLocalStorage();
            this.updateWishlistUI();
            alert(`${product.title} added to wishlist!`);
        }
    },
    
    removeItem: function(productId) {
        this.items = this.items.filter(item => item.id !== productId);
        this.saveToLocalStorage();
        this.updateWishlistUI();
    },
    
    saveToLocalStorage: function() {
        localStorage.setItem('shopnow-wishlist', JSON.stringify(this.items));
    },
    
    loadFromLocalStorage: function() {
        const savedWishlist = localStorage.getItem('shopnow-wishlist');
        if (savedWishlist) {
            this.items = JSON.parse(savedWishlist);
        }
    },
    
    updateWishlistUI: function() {
        // Update wishlist count if element exists
        const wishlistElement = document.querySelector('.wishlist-count');
        if (wishlistElement) {
            wishlistElement.textContent = this.items.length;
        }
    }
};

// Initialize wishlist manager when DOM is loaded
document.addEventListener('DOMContentLoaded', function() {
    wishlistManager.loadFromLocalStorage();
});

// Export utils and managers for potential use in other modules
if (typeof module !== 'undefined' && module.exports) {
    module.exports = { 
        utils, 
        cartManager, 
        wishlistManager 
    };
}