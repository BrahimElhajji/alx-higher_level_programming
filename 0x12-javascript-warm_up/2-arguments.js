#!/usr/bin/node
const Args = process.argv.length;
if (Args === 2) {
  console.log('No argument');
} else if (Args === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
