"use strict";
class Pointer {
    constructor(x, y) {
        this.x = x;
        this.y = y;
    }
    getPoint() {
        return `(${this.x}, ${this.y})`;
    }
}
//private fields
class C {
    constructor(length) {
        this._length = length;
    }
    getLength() {
        return this._length;
    }
}
// Inheritance example
class Shape {
    constructor(color) {
        this.color = color;
    }
    getColor() {
        return this.color;
    }
}
class Circle extends Shape {
    constructor(color, radius) {
        super(color);
        this.radius = radius;
    }
    getArea() {
        return Math.PI * this.radius * this.radius;
    }
}
class Rectangle extends Shape {
    constructor(color, width, height) {
        super(color);
        this.width = width;
        this.height = height;
    }
    getArea() {
        return this.width * this.height;
    }
}
class Sonar {
    ping() {
        console.log("ping");
    }
}
let s = new Sonar();
s.ping();
let redCircle = new Circle("red", 5);
console.log(redCircle.getColor()); // Output: red
console.log(redCircle.getArea()); // Output: 78.53981633974483
let blueRectangle = new Rectangle("blue", 3, 4);
console.log(blueRectangle.getColor()); // Output: blue
console.log(blueRectangle.getArea()); // Output: 12
let x = new Pointer(3, 7);
let y = new Pointer("Hello", "World");
let z = new Pointer(3);
console.log(x.getPoint());
console.log(y.getPoint());
console.log(z.getPoint());
let c = new C(10);
console.log(c.getLength());
