"use strict";
let obj = { x: 0 };
// None of the following lines of code will throw compiler errors.
// Using `any` disables all further type checking, and it is assumed
// you know the environment better than TypeScript.
// Using dot notation
console.log(obj.x); // Outputs: 0
// Using bracket notation
console.log(obj['x']); // Outputs: 0
// obj.foo();
// obj();
obj.bar = 100;
obj = "hello";
const n = obj;
console.log(n);
