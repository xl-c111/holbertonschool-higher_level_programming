#!/usr/bin/node

const args = process.argv.slice(2).map(Number);

if (args.length === 0 || args.length === 1) {
  console.log(0);
} else {
  // initialize max and secondmax to the lowest possible value, so that any number in the array can be larger than them
  let max = -Infinity;
  let secondmax = -Infinity;

  for (const num of args) {
    if (num > max) {
      secondmax = max;
      max = num;
    } else if (num > secondmax && num < max) {
      secondmax = num;
    }
  }
  console.log(secondmax);
}

// Convert each argument to a number during iteration by using Number()
/*
const args = process.argv.slice(2);

if (args.length < 2) {
  console.log(0);
} else {
  let max = -Infinity;
  let secondmax = -Infinity;

  for (let i = 0; i < args.length; i++) {
    const num = Number(args[i]);
    if (num > max) {
      secondmax = max;
      max = num;
    } else if (num > secondmax && num < max) {
      secondmax = num;
    }
  }
  console.log(secondmax);
}
*/
