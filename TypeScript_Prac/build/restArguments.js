"use strict";
function multiply(n, ...m) {
    return m.map((x) => n * x);
}
// 'a' gets value [10, 20, 30, 40]
const a = multiply(10, 1, 2, 3, 4);
console.log(a);
