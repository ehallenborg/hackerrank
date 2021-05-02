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

function getLetter(s) {
    let letter;
    if (['a', 'e', 'i', 'o', 'i'].includes(s[0])) {
        letter = 'A'
    } else if (['b', 'c', 'd', 'f', 'g'].includes(s[0])) {
        letter = 'B'
    } else if (['h', 'j', 'k', 'l', 'm'].includes(s[0])) {
        letter = 'C'
    } else {
        letter = 'D'
    }
    return letter;
}


function main() {
    const s = readLine();
    
    console.log(getLetter(s));
}