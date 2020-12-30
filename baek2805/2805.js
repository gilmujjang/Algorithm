// const fs = require('fs');
// const input = fs.readFileSync('/dev/stdin').toString().trim().split('');

const input = ['4', '7', '20', '15', '10', '17']

const n = input.shift();
const need = input.shift();

let ans = 0;


let height = parseInt(Math.min(...input))
for(i=0; i<input.length; i++){
    ans = ans + parseInt(input[i])-height
}
console.log(ans)