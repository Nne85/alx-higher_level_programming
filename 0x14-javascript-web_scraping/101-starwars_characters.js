#!/usr/bin/node
const request = require('request');

const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else if (response.statusCode !== 200) {
    console.error(`Error: Received status code ${response.statusCode}`);
  } else {
    const movieData = JSON.parse(body);
    const characters = movieData.characters;

    // Function to fetch character names from URLs
    function fetchCharacterName(url) {
      return new Promise((resolve, reject) => {
        request.get(url, (error, response, body) => {
          if (error) {
            reject(error);
          } else if (response.statusCode !== 200) {
            reject(new Error(`Error: Received status code ${response.statusCode}`));
          } else {
            const characterData = JSON.parse(body);
            resolve(characterData.name);
          }
        });
      });
    }

    // Array to store promises for fetching character names
    const characterPromises = characters.map((characterUrl) => fetchCharacterName(characterUrl));

    // Resolve all promises and display character names
    Promise.all(characterPromises)
      .then((characterNames) => {
        characterNames.forEach((name) => console.log(name));
      })
      .catch((error) => {
        console.error(error);
      });
  }
});
