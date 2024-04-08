#!/usr/bin/node
const Args = process.argv[2];

const number = parseInt(Args);

if (!isNaN(number)) {
  console.log('My number: ' + number);
} else {
  console.log('Not a number');
}
