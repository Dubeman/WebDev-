"use strict";
//Demonstrate the use of generics in TypeScript
function identity(arg) {
    return arg;
}
let str1 = identity("myString");
let num1 = identity(123);
console.log(str1);
console.log(num1);
function longest(a, b) {
    if (a.length >= b.length) {
        return a;
    }
    else {
        return b;
    }
}
// longerArray is of type 'number[]'
const longerArray = longest([1, 2], [1, 2, 3]);
// longerString is of type 'alice' | 'bob'
const longerString = longest("alice", "bob");
