#!/usr/bin/node

const request = require('request');

request(process.argv[2], (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const number = JSON.parse(body).results.filter((item) => {
      return item.characters.filter((url) => {
        return url.includes('18');
      }).length;
    }).length;
    console.log(number);
  }
});
