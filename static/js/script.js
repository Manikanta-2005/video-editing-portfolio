document.addEventListener("DOMContentLoaded", () => {

    /* =========================
       NAVBAR
    ========================= */

    const navbar = document.getElementById("navbar");

    window.addEventListener("scroll", () => {

        if (window.scrollY > 50) {
            navbar.classList.add("scrolled");
        } else {
            navbar.classList.remove("scrolled");
        }

    });


    /* =========================
       MOBILE MENU
    ========================= */

    const menuToggle = document.getElementById("menuToggle");
    const navMenu = document.getElementById("navMenu");

    menuToggle.addEventListener("click", () => {

        navMenu.classList.toggle("active");

    });


    /* Close mobile menu after clicking a link */

    const navLinks = document.querySelectorAll(".nav-menu a");

    navLinks.forEach(link => {

        link.addEventListener("click", () => {

            navMenu.classList.remove("active");

        });

    });


    /* =========================
       SCROLL REVEAL
    ========================= */

    const revealElements = document.querySelectorAll(
        ".project-card, .service-card, .about-content, .contact-box"
    );

    const revealObserver = new IntersectionObserver(
        (entries, observer) => {

            entries.forEach(entry => {

                if (entry.isIntersecting) {

                    entry.target.classList.add("reveal");

                    observer.unobserve(entry.target);

                }

            });

        },
        {
            threshold: 0.15
        }
    );


    revealElements.forEach(element => {

        revealObserver.observe(element);

    });


    /* =========================
       SHOWREEL BUTTON
    ========================= */

    const playButton = document.getElementById("playButton");

    playButton.addEventListener("click", () => {

        alert(
            "Your showreel video will be connected here."
        );

    });


    /* =========================
       PROJECT HOVER EFFECT
    ========================= */

    const projectCards = document.querySelectorAll(".project-card");

    projectCards.forEach(card => {

        card.addEventListener("mouseenter", () => {

            card.style.transition = "transform 0.3s ease";

        });

    });


    /* =========================
       CURRENT YEAR
    ========================= */

    const currentYear = new Date().getFullYear();

    console.log(
        `Mani Portfolio — ${currentYear}`
    );

});