#!/usr/bin/node
const fs = require('request');

fs('https://swapi-api.alx-tools.com/api/films/' + process.argv.slice(2)[0], function (error, body) {
    if (error) {
        console.log(error);
      }
  for (const wars of JSON.parse(body).results) {
    console.log(wars.characters);
    }
});
