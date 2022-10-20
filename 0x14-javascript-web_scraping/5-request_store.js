#!/usr/bin/node

const fs = require('fs');
const request = require('request');

request(process.argv[2], (error, response, body) => {
  if (error) {
    console.error(error);
  }
  try {
    fs.writeFile(process.argv[3], body, 'utf8', (err, data) => {
      console.log(err);
    });
  } catch (err) {
    console.log(err);
  }
});
