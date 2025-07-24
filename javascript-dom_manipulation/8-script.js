document.addEventListener('DOMContentLoaded', () => {
  fetch('http://localhost:3000/api/hello?lang=fr')
    .then((response) => response.json())
    .then((data) => {
      const helloDiv = document.getElementById('hello');
      if (data.hello) {
        helloDiv.textContent = data.hello;
      } else if (data.error) {
        helloDiv.textContent = data.error;
      } else {
        helloDiv.textContent = 'Unknown response';
      }
    })
    .catch((error) => {
      console.error('Fetch error:', error);
      document.getElementById('hello').textContent = 'Request failed';
    });
});




// fetch('https://hellosalut.stefanbohacek.dev/?lang=fr')
//   .then((response) => response.json())
//   .then((data) => {
//     document.getElementById('hello').textContent = data.hello;
//   })
//   .catch((error) => console.error('Error:', error));

