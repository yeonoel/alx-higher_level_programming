#!/usr/bin/node

const fs = require('fs');
const request = require('request');

request(process.argv[2], (error, response, body) => {
  if (error) {
    console.log(error);
  }
  try {
    fs.writeFile(process.argv[3], body, 'utf8', err => {
      console.log(err);
    });
  } catch (err) {
    console.log(err);
  }
});
