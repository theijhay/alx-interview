#!/usr/bin/node

const request = require('request');

const movie = process.argv[2];
const StarPoint = 'https://swapi-api.hbtn.io/api/films/' + movie;
let person = [];
const namee = [];

const requestCharacters = async () => {
  await new Promise(resolve => request(StarPoint, (err, res, body) => {
    if (err || res.statusCode !== 200) {
      console.error('Error: ', err, '| StatusCode: ', res.statusCode);
    } else {
      const jsonBody = JSON.parse(body);
      person = jsonBody.characters;
      resolve();
    }
  }));
};

const requestNames = async () => {
  if (person.length > 0) {
    for (const p of person) {
      await new Promise(resolve => request(p, (err, res, body) => {
        if (err || res.statusCode !== 200) {
          console.error('Error: ', err, '| StatusCode: ', res.statusCode);
        } else {
          const jsonBody = JSON.parse(body);
          namee.push(jsonBody.name);
          resolve();
        }
      }));
    }
  } else {
    console.error('Error: Got no Characters for some reason');
  }
};

const getCharNames = async () => {
  await requestCharacters();
  await requestNames();

  for (const n of namee) {
    if (n === namee[namee.length - 1]) {
      process.stdout.write(n);
    } else {
      process.stdout.write(n + '\n');
    }
  }
};

getCharNames();
