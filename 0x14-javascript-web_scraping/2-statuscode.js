#!/usr/bin/node
const request = require('axios');
const argv2 = process.argv[2];
request.get(argv2, get);
function get (notfound, argv2) { if (argv2) { console.log('code: ' + argv2.statusCode || notfound); } }
