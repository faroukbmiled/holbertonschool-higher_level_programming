#!/usr/bin/node
const file = require('fs');
file.readFile(process.argv[2], 'utf8', read);
function read (notfound, found) {
  console.log(notfound || found);
}
