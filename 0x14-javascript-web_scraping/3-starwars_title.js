#!/usr/bin/node
const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request.get(apiUrl, function (error, response, body) {
  if (error) {
    console.log(error);
  } else if (response.statusCode !== 200) {
    console.log(`Error: Received status code ${response.statusCode}`);
  } else {
    const movieData = JSON.parse(body);
    console.log(movieData.title);
  }
});
