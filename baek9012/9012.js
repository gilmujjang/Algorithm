//let fs = require('fs');
//let input = fs.readFileSync('/dev/stdin').toString().split('\n');

const input = [
  '6',
  '(())())',
  '(((()())()',
  '(()())((()))',
  '((()()(()))(((())))()',
  '()()()()(()()())()',
  '(()((())()('
];


for(i=1; i<input.length; i++){
  let num = 0;
  if(input[i].length%2==0){
    for(j=0; j<input[i].length; j++){
      if(input[i][j]=="("){
        num++;
      } else {
        num--;
      }
    }
    if(num==0){
      console.log("YES");
    } else {
      console.log("NO")
    } 
  } else {
    console.log("NO")
  }
  
}