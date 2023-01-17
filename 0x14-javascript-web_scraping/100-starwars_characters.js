#!/usr/bin/node
const fs = require('request');
const fcx = require('request');

fs('https://swapi-api.alx-tools.com/api/films/' + process.argv.slice(2)[0], function (error, response, body) {
    if (error) {
        console.log(error);
      }
  for (const wars of JSON.parse(body).characters) {
    fcx(wars, function (error, response, body){
	if (error) {
	console.log(error);
	}
	console.log(JSON.parse(body).name);
	});
    }
});
