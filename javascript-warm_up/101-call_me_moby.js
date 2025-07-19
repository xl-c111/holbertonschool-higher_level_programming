#!/usr/bin/node

exports.callMeMoby = function (x, theFunction) {
  for (let i = 0; i < x; i++) {
    theFunction();
  }
};



// Use while loop to execute x times function 
/* 
exports.callMeMoby = function (x, theFunction) {
  let i = 0;
  while (i < x) {
    theFunction();
    i++;
  }
}
*/