
//Header scrolling 
const header = document.querySelector('header');
let navbar_logo = document.querySelector('.header-logo img');
const navLinks = document.querySelectorAll('.nav-link');


window.addEventListener('scroll', () => {
  if (window.scrollY > 0) {
    header.classList.add('navbar-scrolled');
    navbar_logo.src = "static/images/logo%20-primary%20-transparent%20-horizontal.png";
    // navLinks.forEach(link => 
    //     {
    //     link.classList.remove('lighten-link')
    //     link.classList.add('darken-link')

    //     }
    // );


  } else {
    header.classList.remove('navbar-scrolled');
    navbar_logo.src = "static/images/logo%20-white%20-transparent%20-horizontal.png"
    // navLinks.forEach(
    //     link => {
    //         link.classList.add('lighten-link')
    //         link.classList.remove('darken-link')
    //     }
    // );



  }
}); 