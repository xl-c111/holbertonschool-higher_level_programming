#!/usr/bin/node

const args = process.argv[2];
const num = parseInt(args);

function facturial (n) {
  if (n === 0 || n === 1) {
    return 1;
  } else {
    return n * facturial(n - 1);
  }
}

if (!isNaN(num)) {
  console.log(facturial(num));
} else {
  console.log(1);
}
