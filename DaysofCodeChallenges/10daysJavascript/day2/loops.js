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
 * Complete the vowelsAndConsonants function.
 * Print your output using 'console.log()'.
 */
function vowelsAndConsonants(s) {
    var vowels = ['a', 'e', 'i', 'o', 'u']

    for (var t=0; t < s.length; t++) {
        if (vowels.includes(s[t])) {
            console.log(s[t])
        }
    }

    for(var i=0; i < s.length;i++) {
        if (vowels.includes(s[i]) == false) {
            console.log(s[i])
        }
    }
}

