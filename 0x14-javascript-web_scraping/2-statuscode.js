#!/usr/bin/node

const request = require('request');

request(process.argv[2], function (error, resp) {
  console.error('error:', error);
  console.log('code:', resp && resp.statusCode);
});
