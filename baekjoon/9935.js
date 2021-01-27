//let fs = require('fs');
//let input = fs.readFileSync('/dev/stdin').toString().split('\n');
// let original = input[0];
// let bomb = input[1];
let ans;
let original = 'mirkovC4nizCC44';
let bomb = 'C4';

function explosion(original, bomb){
  let ori = original.split('');
  for(i=0; i<ori.length; i++){
    let b = false;
    if(ori[i]==bomb[0]){
      for(j=1; j<bomb.length; j++){
        if(ori[i+j]==bomb[j]){
          b = true;
        } else {
          b = false;
          break
        }
      }
      if(b){
        for(j=0; j<bomb.length; j++){
          ori.splice(i,1);
        }
        original = ori.join('');
        ans = original;
        explosion(original,bomb)
      }
    }
  }
}

explosion(original,bomb)
if(ans==''){
  console.log("FRULA")
} else {
  console.log(ans);
}

