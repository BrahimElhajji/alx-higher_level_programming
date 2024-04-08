#!/usr/bin/node
function add (a, b) {
  return a + b;
}

const Args1 = process.argv[2];
const Args2 = process.argv[3];
const a = parseInt(Args1);
const b = parseInt(Args2);

console.log(add(a, b));
