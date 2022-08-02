#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let out = '';
    for (let i = 0; i < this.width; i++) out += 'X';
    for (let x = 0; x < this.height; x++) {
      console.log(out);
    }
  }
};
