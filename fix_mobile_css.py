with open("styles.css", "r", encoding="utf-8") as f:
    content = f.read()

new_css = '''
/* Hamburger Menu & Mobile Navbar Fixes */
@media (max-width: 768px) {
    .navbar-desktop-row {
        position: relative;
    }
    .logo-new {
        position: absolute;
        left: 50%;
        transform: translateX(-50%);
        margin: 0;
    }
    .nav-actions-new {
        margin-left: auto; /* push icons to the right */
        gap: 0.5rem;
    }
    .nav-links-new {
        position: fixed;
        top: 0;
        left: -100%;
        width: 80%;
        max-width: 300px;
        height: 100vh;
        background: #fff;
        flex-direction: column;
        justify-content: flex-start;
        align-items: flex-start;
        padding: 5rem 2rem 2rem;
        gap: 2rem;
        box-shadow: 2px 0 10px rgba(0,0,0,0.1);
        transition: left 0.3s ease;
        z-index: 1000;
        margin: 0;
    }
    .nav-links-new.active {
        left: 0;
    }
    .menu-toggle {
        display: block !important;
        cursor: pointer;
        z-index: 1001;
    }
    .close-menu-btn {
        display: block !important;
        position: absolute;
        top: 1rem;
        right: 1rem;
        background: none;
        border: none;
        font-size: 2rem;
        cursor: pointer;
    }
}
@media (min-width: 769px) {
    .menu-toggle {
        display: none !important;
    }
    .close-menu-btn {
        display: none !important;
    }
}
'''
content += new_css

with open("styles.css", "w", encoding="utf-8") as f:
    f.write(content)
