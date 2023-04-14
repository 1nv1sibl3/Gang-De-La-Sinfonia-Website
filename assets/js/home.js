// Made by Om Honrao aka Inv1s1bl3 

// JavaScript for hover menu functionality
var menuToggle = document.getElementById('menuToggle');
var hoverMenu = document.getElementById('hoverMenu');
var menuOverlay = document.getElementById('menuOverlay');
var closeBtn = document.getElementById('closeBtn');
var body = document.body;

menuToggle.addEventListener('click', function() {
  this.classList.toggle('open');
  hoverMenu.classList.toggle('active');
  menuOverlay.classList.toggle('active');
  closeBtn.classList.toggle('active'); // Add this line
  body.classList.toggle('active');
});

closeBtn.addEventListener('click', function() {
  menuToggle.classList.remove('open');
  hoverMenu.classList.remove('active');
  menuOverlay.classList.remove('active');
  closeBtn.classList.remove('active'); // Add this line
  body.classList.remove('active');
});
