#!/usr/bin/node
const request = require('request');
const file = require('fs');
request(process.argv[2], function (n, x, body) { file.writeFile(process.argv[3], body, 'utf-8', function () { }); });
