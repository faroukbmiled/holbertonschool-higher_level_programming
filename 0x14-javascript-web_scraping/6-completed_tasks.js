#!/usr/bin/node
const request = require('request');
request(process.argv[2], function (x, n, body) {
  const data = {};
  for (const resp of JSON.parse(body)) {
    if (resp.completed) {
      if (data[resp.userId]) {
        data[resp.userId] += 1;
      } else {
        data[resp.userId] = 1;
      }
    }
  }
  console.log(data);
});
