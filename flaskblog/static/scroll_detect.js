let lastScrollY = window.scrollY;
const banner = document.querySelector('.banner');

window.addEventListener('scroll', () => {
  const currentScrollY = window.scrollY;

  if (currentScrollY < lastScrollY) {
    // Scrolling up
    banner.classList.add('visible');
  } else {
    // Scrolling down
    banner.classList.remove('visible');
  }

  lastScrollY = currentScrollY;
});
