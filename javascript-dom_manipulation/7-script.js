fetch('https://swapi-api.hbtn.io/api/films/?format=json')
  .then((response) => response.json())
  .then((data) => {
    const movies = data.results;
    const movieList = document.getElementById('list_movies');

    movies.forEach((movie) => {
      const li = document.createElement('li');
      li.textContent = movie.title;
      movieList.appendChild(li);
    });
  })
  .catch((error) => console.error('Error:', error));
