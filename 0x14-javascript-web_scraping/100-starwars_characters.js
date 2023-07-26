#!/usr/bin/node
const request = require('request');

const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const movieData = JSON.parse(body);
    const characterUrls = movieData.characters;

    // Function to get character name from character URL
    const getCharacterName = (url) => {
      return new Promise((resolve, reject) => {
        request.get(url, (error, response, body) => {
          if (error) {
            reject(error);
          } else {
            const characterData = JSON.parse(body);
            resolve(characterData.name);
          }
        });
      });
    };

    // Fetch character names in parallel using Promise.all
    Promise.all(characterUrls.map(getCharacterName))
      .then((characterNames) => {
        characterNames.forEach((name) => console.log(name));
      })
      .catch((error) => {
        console.error(error);
      });
  }
});
