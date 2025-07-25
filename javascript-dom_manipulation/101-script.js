document.addEventListener('DOMContentLoaded', () => {
  const languageCode = document.getElementById('language_code');
  const translateButton = document.getElementById('btn_translate');
  const hello = document.getElementById('hello');

  translateButton.addEventListener('click', function () {
    const lang = languageCode.value;
    if (!lang) {
      hello.textContent = 'Please select a language';
      return;
    }

    fetch(`https://hellosalut.stefanbohacek.com/?lang=${lang}`)
      .then((response) => response.json())
      .then((data) => {
        hello.textContent = data.hello;
      })
      .catch((error) => console.error('Error:', error));
  });
});
