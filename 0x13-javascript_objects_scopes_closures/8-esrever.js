#!/usr/bin/node
/**
 * function to reverse a list
 * @param {list} list - list to reverse
 * @returns {list} reversed list
 */
exports.esrever = function (list) {
  const newList = [];
  for (let i = list.length - 1; i >= 0; i--) {
    newList.push(list[i]);
  }
  return newList;
}
