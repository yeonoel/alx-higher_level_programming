#!/usr/bin/node
exports.esrever = function (list) {
  let c = 1;
  let x;
  const midSize = Math.round(list.length / 2);
  for (let i = 0; i < midSize; i++) {
    x = list[i];
    list[i] = list[list.length - c];
    list[list.length - c] = x;
    c++;
  }
  return (list);
};
