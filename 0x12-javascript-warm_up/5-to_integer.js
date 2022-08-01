#!/usr/bin/node
n = process.argv
if (!parseInt(n[2])) {
  console.log('Not a number');
} else {
  console.log('My number: ' + n[2]);
}
