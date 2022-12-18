#!/usr/bin/node

let sbj = 'undefined';
let obj = 'undefined';
if (process.argv[2]) {
  sbj = process.argv[2];
} if (process.argv[3]) {
  obj = process.argv[3];
}
console.log(sbj + ' is ' + obj);
