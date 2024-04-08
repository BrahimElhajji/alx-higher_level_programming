#!/usr/bin/node
function factorial (n) {
  if (isNaN(n) || n === 1) {
    return 1;
  }
  return n * factorial(n - 1);
}
const Args = process.argv[2];

const num = parseInt(Args);

console.log(factorial(num));
