"use strict";
let obj1 = { x: 0 };
// None of the following lines of code will throw compiler errors.
// Using `any` disables all further type checking, and it is assumed
// you know the environment better than TypeScript.
// Using dot notation
console.log(obj1.x); // Outputs: 0
// Using bracket notation
console.log(obj1['x']); // Outputs: 0
// obj.foo();
// obj();
obj1.bar = 100;
obj1 = "hello";
const n = obj1;
console.log(n);
//write the code for different data types and data structures in typescript
// Different data types
let num = 10;
let str = "hello";
let bool = true;
let arr = [1, 2, 3];
let tuple = ["apple", 5];
var Color;
(function (Color) {
    Color[Color["Red"] = 0] = "Red";
    Color[Color["Green"] = 1] = "Green";
    Color[Color["Blue"] = 2] = "Blue";
})(Color || (Color = {}));
;
let enumValue = Color.Red;
let anyValue = "dynamic value";
// Data structures
let obj = { x: 0 };
let map = new Map();
map.set("key1", 1);
map.set("key2", 2);
let set = new Set();
set.add(1);
set.add(2);
let stack = [];
stack.push(1);
stack.push(2);
let queue = [];
queue.push(1);
queue.push(2);
console.log("Popped number: ", queue.shift());
console.log("map.get('key1'): ", map.get("key1"));
// import { LinkedList } from './linkedList'; // Assuming the LinkedList class is defined in a separate file called 'linkedList.ts'
// let linkedList: LinkedList<number> = new LinkedList();
// linkedList.add(1);
// linkedList.add(2);
