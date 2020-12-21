//let fs = require('fs');
//let input = fs.readFileSync('/dev/stdin').toString().split('\n');

const input = [
  '14',
  'push', '1',
  'push', '2',
  'top',
  'size',
  'empty',
  'pop',
  'pop',
  'pop',
  'size',
  'empty',
  'pop',
  'push', '3',
  'empty',
  'top'
]
let num = [];
let s = 0;


for(i=1; i<input.length; i++){
  let now = input[i];
  let next = input[i+1];
  if(input[i]=='push'){
    num.push(next);
    s = s + 1;
  }
  if(now=='pop'){
    if(s>0){
      console.log(num.pop());
      s = s - 1;
    } else {
      console.log(-1)
    }
  }
  if(now=='size'){
    console.log(s);
  }
  if(now=='empty'){
    if(s>0){
      console.log(0)
    } else {
      console.log(1)
    }
  }
  if(now=='top'){
    if(s>0){
      console.log(num[s-1]);
    } else {
      console.log(-1);
    }
  }
}