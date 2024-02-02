function ToggleNavvbar() {
    document.querySelector(".main-menu").classList.toggle("show");
}
document.querySelector(".menu-btn").addEventListener("click", ToggleNavvbar);

var slideIndex = 1;
showDivs(slideIndex);

const menuIcon = document.querySelector('#menu-icon');
const navbar = document.querySelector('.navbar');
const navbg = document.querySelector('.nav-bg');
menuIcon.addEventListener('click', () => {
    menuIcon.classList.toggle('bx-x');
    navbar.classList.toggle('active');
    navbg.classList.toggle('active');
});