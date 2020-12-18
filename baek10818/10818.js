//let fs = require('fs');
//let input = fs.readFileSync('/dev/stdin').toString().split('\n');
input = ['5',
  '20 10 35 30 7'
]
const x = input[1].split(' ');
let num = [];
for(i=0; i<x.length; i++){
  num.push(parseInt(x[i]))
}
const max = Math.max(...num);
const min = Math.min(...num);
console.log(min,"",max);

//runtime error남