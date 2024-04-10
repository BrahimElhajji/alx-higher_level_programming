#!/usr/bin/node

exports.converter = function (base) {
  return function (nm) {
    return nm.toString(base);
  };
};
