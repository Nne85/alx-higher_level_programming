#!/usr/bin/node

function findSecondBiggest (numbers) {
  if (numbers.length < 2) {
    return 0;
  }

  let max = -Infinity;
  let secondMax = -Infinity;

  for (let i = 0; i < numbers.length; i++) {
    const num = parseInt(numbers[i]);

    if (num > max) {
      secondMax = max;
      max = num;
    } else if (num > secondMax && num < max) {
      secondMax = num;
    }
  }

  return secondMax;
}

const args = process.argv.slice(2);

console.log(findSecondBiggest(args));
