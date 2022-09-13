#!/usr/bin/node
const request = require('request');
request(process.argv[2], function (nf, none, resp) {
  if (nf); let i = 0;
  for (const response of JSON.parse(resp).results) {
    for (const char of response.characters) {
      i += (char.includes('18'));
    }
  }
  console.log(i);
});
