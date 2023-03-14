#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0) {
      return {};
    } else {
      this.width = w;
      this.height = h;
    }
  }
};
