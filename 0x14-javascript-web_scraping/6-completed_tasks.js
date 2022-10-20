#!/usr/bin/node

const request = require('request');

request(process.argve[2], (error, reponse, body) => {
  if (error) {
    console.error(error);
  }
  const dic = JSON.parse(body).reduce((acc, curr) => {
    if (!acc[curr.userId]) {
      if (curr.completed) {
        acc[curr.userId] = 1;
      }
    } else {
      if (curr.completed) {
        acc[curr.userId] += 1;
      }
    }
    return acc;
  }, {});
  console.log(dic);
});
