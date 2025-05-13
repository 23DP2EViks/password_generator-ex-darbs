
document.addEventListener('DOMContentLoaded', () => {
  const burger = document.getElementById('burger');
  const navLinks = document.querySelector('.nav-links');

  burger.addEventListener('click', (e) => {
    e.stopPropagation();
    navLinks.classList.toggle('active');
    burger.classList.toggle('open');
  });

  document.addEventListener('click', (e) => {
    if (!navLinks.contains(e.target) && !burger.contains(e.target)) {
      navLinks.classList.remove('active');
      burger.classList.remove('open');
    }
  });

  navLinks.querySelectorAll('a').forEach(link => {
    link.addEventListener('click', () => {
      navLinks.classList.remove('active');
      burger.classList.remove('open');
    });
  });
});
