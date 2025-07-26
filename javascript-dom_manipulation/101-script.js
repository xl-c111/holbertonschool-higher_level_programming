document.addEventListener('DOMContentLoaded', () => {
  const languageCode = document.getElementById('language_code');
  const translateButton = document.getElementById('btn_translate');
  const hello = document.getElementById('hello');

  translateButton.addEventListener('click', function () {
    const language = languageCode.value;
    if (!language) {
      hello.textContent = 'Please select a language';
      return;
    }

    fetch(`https://hellosalut.stefanbohacek.com/?lang=${language}`)
      .then((response) => response.json())
      .then((data) => {
        hello.textContent = data.hello;
      })
      .catch((error) => console.error('Error:', error));
  });
});
