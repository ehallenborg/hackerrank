'use strict';

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', inputStdin => {
    inputString += inputStdin;
});

process.stdin.on('end', _ => {
    inputString = inputString.trim().split('\n').map(string => {
        return string.trim();
    });
    
    main();    
});

function readLine() {
    return inputString[currentLine++];
}

/*
 * Complete the isPositive function.
 * If 'a' is positive, return "YES".
 * If 'a' is 0, throw an Error with the message "Zero Error"
 * If 'a' is negative, throw an Error with the message "Negative Error"
 */
function isPositive(a) {
    if (a > 0) {
        return 'YES';
    }
    else {
        throw (a === 0 ? new Error('Zero Error') : new Error('Negative Error'));
    }
}

function isPositiveII(a) {
    // use if you're 100% sure that the inputs are all numbers
    if (a > 0) { return "YES" };
    throw Error (a ? "Negative Error" : "Zero Error");
}

