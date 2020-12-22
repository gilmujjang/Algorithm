//let fs = require('fs');
//let input = fs.readFileSync('/dev/stdin').toString().split('\n');

const input = '(((()(()()))(())()))(()())';
let num = 0;
let ans = 0;
let sta = false;

for(i=0; i<input.length; i++){
  if(input[i]=="("){
    num++;
    sta = true;
  } else {
    if(sta){
      ans = ans + (num-1);
      num--;
      sta=false;
    } else {
      num--;
      ans++;
      sta=false;
    }
  }
}
console.log(ans);
