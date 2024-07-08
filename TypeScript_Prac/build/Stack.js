"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.Stack = void 0;
class Stack {
    constructor() {
        this.elements = [];
    }
    push(element) {
        this.elements.push(element);
    }
    pop() {
        return this.elements.pop();
    }
    isEmpty() {
        return this.elements.length === 0;
    }
    printStack() {
        this.elements.forEach((element) => console.log(element));
    }
}
exports.Stack = Stack;
const numberStack = new Stack();
numberStack.push(1);
numberStack.push(2);
numberStack.push(3);
console.log("Printing number stack : ");
numberStack.printStack();
console.log("Popping from number stack : ");
console.log(numberStack.pop());
console.log(numberStack.pop());
console.log("Printing number stack : ");
numberStack.printStack();
console.log(numberStack.pop());
console.log(numberStack.pop());
