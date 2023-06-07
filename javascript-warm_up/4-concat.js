#!/usr/bin/node
const args = process.argv.slice(2);
const numArgs = args.length;

if (numArgs >= 2) {
  console.log(args[0] + ' is ' + args[1]);
} else {
  console.log('HBTN is undefined');
}
