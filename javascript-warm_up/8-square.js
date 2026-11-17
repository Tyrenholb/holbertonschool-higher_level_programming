#!/usr/bin/node

const x = process.argv[2];
let i = 0;
let row = '';
let j = 0;
const num = Number(x);

if (Number.isNaN(num)) {
  console.log('Missing size');
}

while (i < num) {
  j = 0;
  row = '';
  while (j < num) {
    row += 'x';
    j++;
  }
  console.log(row);
  i++;
}
