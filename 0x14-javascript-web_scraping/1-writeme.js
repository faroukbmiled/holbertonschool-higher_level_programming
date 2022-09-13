#!/usr/bin/node
const file = require('fs');
const argv3 = process.argv[3];
file.writeFile(process.argv[2], argv3, write);
function write (write) { if (write) console.log(write); }
