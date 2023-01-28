'use strict';
$(() => {
  const API_URL = 'https://swapi-api.hbtn.io/api';

  $.get(`${API_URL}/people/5/?format=json`, (data, status) => {
    $('DIV#character').html(data.name);
  });
});
