#!/usr/bin/node

const x = process.argv[2];
let i = 0;
const num = Number(x);

if (Number.isNaN(num)) {
  console.log('Missing number of occurrences');
}
while (i < num) {
  console.log('C is fun');
  i++;
}
