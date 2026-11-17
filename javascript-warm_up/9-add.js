#!/usr/bin/node

let x = 0;
const a = Number(process.argv[2]);
const b = Number(process.argv[3]);

function add (a, b) {
  x = a + b;
  return console.log(x);
}
add(a, +b);
