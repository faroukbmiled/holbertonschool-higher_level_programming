#!/usr/bin/node
const request = require('request');
const argv2 = process.argv[2];
request(argv2, get);
function get (notfound, argv2) { if (argv2) { console.log('code: ' + argv2.statusCode || notfound); } }
