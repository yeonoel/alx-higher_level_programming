#!/usr/bin/node
function fact (n) {
  if (n === 0) {
    return (1);
  }
  return (n * fact(n - 1));
}
const num = process.argv[2];
console.log(isNaN(num) ? 1 : fact(num));
