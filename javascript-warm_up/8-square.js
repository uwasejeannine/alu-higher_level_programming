#!/usr/bin/node
if (number) {
  for (let i = 0; i < number; i++) {
    console.log('X'.repeat(number));
  }
} else if (number < 0) {
  console.log();
} else {
  console.log('Missing size');
}
