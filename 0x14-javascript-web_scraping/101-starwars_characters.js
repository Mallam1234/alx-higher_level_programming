#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];

if (!movieId) {
  console.error('Please provide a valid Movie ID as an argument.');
  process.exit(1);
}

const baseUrl = 'https://swapi.dev/api/films/';

request(`${baseUrl}${movieId}/`, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    process.exit(1);
  }

  if (response.statusCode !== 200) {
    console.error('Invalid response:', response.statusCode);
    process.exit(1);
  }

  const movieData = JSON.parse(body);
  const characters = movieData.characters;

  if (characters.length === 0) {
    console.error('No characters found for this movie.');
    process.exit(1);
  }

  fetchCharacters(characters, 0);
});

function fetchCharacters (characters, index) {
  if (index >= characters.length) {
    return;
  }

  request(characters[index], (error, response, body) => {
    if (error) {
      console.error('Error:', error);
    } else {
      const characterData = JSON.parse(body);
      console.log(characterData.name);
    }

    fetchCharacters(characters, index + 1);
  });
}
