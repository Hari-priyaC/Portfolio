document.addEventListener('DOMContentLoaded', () => {
  const loader = document.querySelector('.page-loader');
  setTimeout(() => loader?.classList.add('hidden'), 800);

  AOS.init({ duration: 800, once: true, offset: 80 });

  const typed = new Typed('.typed', {
    strings: ['Python Backend Developer', 'Django Developer', 'FastAPI Developer', 'Full Stack Developer'],
    typeSpeed: 70,
    backSpeed: 40,
    loop: true,
  });

  particlesJS('particles-js', {
    particles: {
      number: { value: 60 },
      color: { value: ['#6c63ff', '#00d9ff', '#ff4d6d'] },
      opacity: { value: 0.4 },
      size: { value: 2.5 },
      line_linked: { enable: true, color: '#00d9ff', opacity: 0.2, width: 1 },
      move: { enable: true, speed: 1.5 }
    },
    interactivity: {
      events: { onhover: { enable: true, mode: 'repulse' } }
    }
  });

  new Swiper('.testimonial-swiper', {
    loop: true,
    autoplay: { delay: 3000 },
    pagination: { el: '.swiper-pagination', clickable: true }
  });

  const cursorGlow = document.querySelector('.cursor-glow');
  document.addEventListener('mousemove', (e) => {
    cursorGlow.style.left = `${e.clientX}px`;
    cursorGlow.style.top = `${e.clientY}px`;
  });

  const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        const counters = entry.target.querySelectorAll('.counter');
        counters.forEach((counter) => {
          const target = +counter.dataset.target;
          let start = 0;
          const step = Math.ceil(target / 80);
          const timer = setInterval(() => {
            start += step;
            if (start >= target) {
              counter.textContent = target;
              clearInterval(timer);
            } else {
              counter.textContent = start;
            }
          }, 25);
        });
        observer.unobserve(entry.target);
      }
    });
  }, { threshold: 0.3 });

  document.querySelectorAll('.stat-card').forEach((card) => observer.observe(card));

  document.querySelectorAll('.filter-btn').forEach((button) => {
    button.addEventListener('click', () => {
      document.querySelectorAll('.filter-btn').forEach((btn) => btn.classList.remove('active'));
      button.classList.add('active');
      const filter = button.dataset.filter;
      document.querySelectorAll('.project-card').forEach((card) => {
        const show = filter === '*' || card.classList.contains(filter);
        card.style.display = show ? '' : 'none';
      });
    });
  });

  const navbar = document.querySelector('.navbar');
  window.addEventListener('scroll', () => {
    navbar.classList.toggle('scrolled', window.scrollY > 50);
    document.querySelectorAll('section').forEach((section) => {
      const top = section.offsetTop - 120;
      const bottom = top + section.offsetHeight;
      if (window.scrollY >= top && window.scrollY < bottom) {
        document.querySelectorAll('.nav-link').forEach((link) => link.classList.toggle('active', link.getAttribute('href') === `#${section.id}`));
      }
    });
  });

  document.getElementById('theme-toggle')?.addEventListener('click', () => {
    document.body.classList.toggle('light');
  });

  const form = document.getElementById('contact-form');
  const success = document.getElementById('contact-success');
  form?.addEventListener('submit', function (e) {
    e.preventDefault();
    const formData = new FormData(this);
    $.ajax({
      url: this.action,
      type: 'POST',
      data: formData,
      processData: false,
      contentType: false,
      headers: { 'X-CSRFToken': $('input[name=csrfmiddlewaretoken]').val() },
      success: () => {
        this.reset();
        success.classList.remove('d-none');
        setTimeout(() => success.classList.add('d-none'), 4000);
      }
    });
  });
});
