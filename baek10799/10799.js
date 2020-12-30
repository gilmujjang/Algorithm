// let fs = require('fs');
// let input = fs.readFileSync('/dev/stdin').toString().split('\n');
// input = input[0]
//이게 뭐하는짓인지 모르겠네;;
const input = '()(((()())(())()))(())';
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
