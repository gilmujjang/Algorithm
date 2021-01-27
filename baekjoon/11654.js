const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().split(' ');
const ans = String(input);

console.log(ans.charCodeAt(0));