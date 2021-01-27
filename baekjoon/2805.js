// const fs = require('fs');
// const input = fs.readFileSync('/dev/stdin').toString().trim().split('');

const input = ['4', '7', '20', '15', '10', '17']

const n = parseInt(input[0]);
const need = parseInt(input[0]);

let ans = 0;
let left = 0;
let right = parstInt(Math.max(...input))
let middle = right/2

while (left<=right){
    middle = (left+right)/2;
    let tree = 0;
    for(i=0; i<n; i++){
        if(middle<)
    }
}

for(i=0; i<input.length; i++){
    ans = ans + parseInt(input[i])-height
}
console.log(ans)