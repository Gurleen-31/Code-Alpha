document.addEventListener('DOMContentLoaded', () => {
    // Example: Scroll to sections when navigation links are clicked
    const links = document.querySelectorAll('nav ul li a');

    links.forEach(link => {
        link.addEventListener('click', (event) => {
            event.preventDefault();
            const sectionID = link.getAttribute('href').substring(1);
            const section = document.getElementById(sectionID);
            section.scrollIntoView({ behavior: 'smooth' });
        });
    });
});
