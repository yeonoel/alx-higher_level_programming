#!/usr/bin/node
if (process.argv.lenght < 2) {
  console.log(0);
} else {
  const args = process.argv.map(Number).slice(2, process.argv.lenght).sort((a, b) => a - b);
  console.log(args[args.length - 2]);
}
