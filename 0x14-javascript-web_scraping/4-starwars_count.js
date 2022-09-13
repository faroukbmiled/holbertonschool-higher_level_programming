#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/people/18/';
request(process.argv[2], function (nf, none, resp) {
  if (nf); let i = 0;
  for (const response of JSON.parse(resp).results) {
    for (const char of response.characters) {
      i += (char.includes(url));
    }
  }
  console.log(i);
});
