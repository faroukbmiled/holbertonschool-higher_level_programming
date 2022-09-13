#!/usr/bin/node
const request = require('request');
const api = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
request(api, function (nf, api, res) { if (api) { console.log(nf || JSON.parse(res).title); } });
