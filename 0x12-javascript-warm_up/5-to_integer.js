#!/usr/bin/node
const arg = process.argv
if (!parseInt(arg[2])) {
  console.log('Not a number');
} else {
  console.log('My number: ' + arg[2]);
}
