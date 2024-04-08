#!/usr/bin/node

const Args = process.argv.slice(2).map(Number);

if (Args.length <= 1) {
  console.log(0);
} else {
  const Sorted = Args.sort((a, b) => b - a);
  console.log(Sorted[1]);
}
