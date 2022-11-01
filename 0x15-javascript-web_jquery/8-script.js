$.get('https://swapi-api.hbtn.io/api/films/?format=json', function (data) {
  $('UL#list_movies').append(...data.results.map(elem => `<li>${elem.title}</li>`));
});
