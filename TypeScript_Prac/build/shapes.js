"use strict";
;
;
;
function getArea(shape) {
    switch (shape.kind) {
        case "circle":
            const circle = shape;
            return Math.PI * circle.radius ** 2;
        case "square":
            const square = shape;
            return square.sideLength ** 2;
    }
}
const cir = { kind: "circle", radius: 10 };
const sq = { kind: "square", sideLength: 7 };
console.log("Area of circle : ", getArea(cir));
console.log("Area of square : ", getArea(sq));
