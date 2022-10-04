#!/usr/bin/node
const initList = require('./100-data').list;
const newList = initList.map((x, index) => x * index);
