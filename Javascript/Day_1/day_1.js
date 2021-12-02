const fs = require("fs");
const puzzleInput = fs
    .readFileSync("./input.txt")
    .toString()
    .split("\n")
    .map((x) => parseInt(x));


function checkDepth(depthMeasurements) {
    let total = 0;
    let lastVal = depthMeasurements[0];
    for (var i = 0; i < depthMeasurements.length; i++) {
        if (depthMeasurements[i] > lastVal) {
            total++;
        }
        lastVal = depthMeasurements[i];
    }
    return total;
}

let totalDepth = checkDepth(puzzleInput)
console.log(`Part 1: ${totalDepth}`)
