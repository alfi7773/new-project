let currentSlide = 0;
const slides = document.querySelectorAll('.slide');
const dots = document.querySelectorAll('.dot');
const prevBtn = document.querySelector('.prev');
const nextBtn = document.querySelector('.next');

function updateSlider() {
  document.querySelector('.slides').style.transform = `translateX(-${currentSlide * 100}%)`;
  dots.forEach((dot, index) => {
    dot.classList.toggle('active', index === currentSlide);
  });
}

prevBtn.addEventListener('click', () => {
  currentSlide = (currentSlide > 0) ? currentSlide - 1 : slides.length - 1;
  updateSlider();
});

nextBtn.addEventListener('click', () => {
  currentSlide = (currentSlide < slides.length - 1) ? currentSlide + 1 : 0;
  updateSlider();
});

dots.forEach((dot, index) => {
  dot.addEventListener('click', () => {
    currentSlide = index;
    updateSlider();
  });
});