#!/usr/bin/node
const size = parseInt(process.argv[2]);
if (!size) {
  console.log('Missing size');
} else {
  for (let i = 0; i < size; i++) {
    let out = '';
    for (let x = 0; x < size; x++) out += 'X';
    console.log(out);
  }
}
