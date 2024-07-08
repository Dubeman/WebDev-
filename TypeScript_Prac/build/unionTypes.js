"use strict";
function printId(id) {
    if (typeof id === "object") {
        // If id is an object, iterate over its properties and print them
        for (const key in id) {
            console.log(`${key}: ${id[key]}`);
        }
    }
    else {
        // If id is not an object, print it directly
        console.log("Your ID is: " + id);
    }
}
// Demonstrating the function with different types
function welcomePeople(x) {
    if (Array.isArray(x)) {
        console.log("Hello, " + x.join(" and "));
    }
    else {
        console.log("Welcome lone traveler " + x);
    }
}
printId(101);
printId("202");
printId({ "movie": 1 });
welcomePeople(["Frodo", "Sam", "Merry", "Pippin"]);
welcomePeople("Sauron");
