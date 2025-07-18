#!/usr/bin/node

exports.addMeMaybe = function (number, theFunction) {
  for (let i = 0; i < number; i++) {
    i += 1;
  }
  theFunction(number + 1);
};
