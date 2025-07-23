const header = document.querySelector('header');
const updateHeader = document.getElementById('update_header');

updateHeader.addEventListener('click', function () {
  header.innerHTML = 'New Header!!!';
});
