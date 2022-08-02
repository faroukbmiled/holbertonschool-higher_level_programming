#!/usr/bin/node

const Rectangle = require('./4-rectangle');
module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      let out = '';
      for (let i = 0; i < this.width; i++) {
        out += 'C';
      }
      for (let x = 0; x < this.height; x++) {
        console.log(out);
      }
    }
  }
};
