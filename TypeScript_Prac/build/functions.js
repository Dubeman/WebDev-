"use strict";
const names = ['Alice', 'Bob', 'Charlie', 'Diana', 'Elvis'];
// 1. Using for loop using anonymous function
names.forEach((name) => { console.log(name.toUpperCase()); });
// The ? after y in the parameter list denotes that the y parameter is optional
function printCoord(pt) {
    console.log(`The coordinate's x value is ${pt.x}`);
    console.log(`The coordinate's y value is ${pt.y}`);
}
printCoord({ x: 3, y: 7 });
printCoord({ x: 3 });
function printName(obj) {
    var _a;
    //   'obj.last' is possibly 'undefined'.
    if (obj.last !== undefined) {
        // OK
        console.log(obj.last.toUpperCase());
    }
    // A safe alternative using modern JavaScript syntax:
    console.log(obj.first.toUpperCase(), " ", (_a = obj.last) === null || _a === void 0 ? void 0 : _a.toUpperCase());
}
printName({ first: "Bob", last: "Marley" });
printName({ first: "Alice" });
