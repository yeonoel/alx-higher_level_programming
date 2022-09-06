#!/usr/bin/node
const xlenght = process.argv.length;
console.log(xlenght === 2 ? 'No argument' : xlenght === 3 ? 'Argument found' : 'Arguments found');
