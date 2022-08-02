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

  rotate () {
    const swap = this.width;
    this.width = this.height;
    this.height = swap;
  }

  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }
};
