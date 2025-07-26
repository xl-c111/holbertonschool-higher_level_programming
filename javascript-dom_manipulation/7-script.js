fetch('https://swapi-api.hbtn.io/api/films/?format=json')
  .then((response) => response.json())
  .then((data) => {
    console.log(data);
    const movies = data.results;
    const movieList = document.getElementById('list_movies');

    movies.forEach((movie) => {
      const li = document.createElement('li');
      li.textContent = movie.title;
      movieList.appendChild(li);
    });
  })
  .catch((error) => console.error('Error:', error));

// for loop
// for(let i = 0; i < movies.length; i++){
//     const li = document.createElement('li');
//     li.textContent = movies[i].title;
//     movieList.appendChild(li);
//   }

// for...of loop
// for (movie of movies) {
//   const li = document.createElement('li');
//   li.textContent = movie.title;
//   movieList.appendChild(li);
// }
