//let fs = require('fs');
//let input = fs.readFileSync('/dev/stdin').toString().split('\n');

let input1 = [
  '4','1 3 5 7 130 13 190 193'
]
let input = input1[1];

let ans = 0;

for(i=1; i<input.length; i++){
  let state = true;
  if(input[i]<2){
    state = false;
  } else {
    for(j=2; j<input[i]; j++){
      if(input[i]%j=='0'){
        state = false;
        break
      }  
    }
  }
  if(state){
    ans++;
  }
}
console.log(ans);
