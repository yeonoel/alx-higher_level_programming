#!/usr/bin/node

const request = require('request');

request('http://swapi.co/api/films/' + process.argv[2], function (err, response, body) {
  if (err) {
    console.error(err);
  }
  JSON.parse(body).characteres.forEach(function (url, callbackfunc) {
    request(url, (error, response, body) => {
      if (error) {
        console.error(error);
      }
      console.log(JSON.parse(body).name);
    });
  });
});
