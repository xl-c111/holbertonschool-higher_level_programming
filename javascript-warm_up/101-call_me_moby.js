#!/usr/bin/node

// exports.callMeMoby = function (x, theFunction) {
//   for (let i = 0; i < x; i++) {
//     theFunction();
//   }
// };

exports.callMeMoby = function (x, theFunction) {
  let i = 0;
  while (i < x) {
    theFunction();
    i++;
  }
};
