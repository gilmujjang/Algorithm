//let fs = require('fs');
//let input = fs.readFileSync('/dev/stdin').toString().split('\n');

const input = "(()[[]])([])";

let asdf = [];
let alpha = 0;
let beta = 0;
let ans = 0;
if(input.length%2!=0){
  console.log(0)
} else {
  for(i=0; i<input.length; i++){
    if(input[i]=="("){
      alpha++;
    } else if(input[i]==")"){
      alpha--;
    } else if(input[i]=="["){
      beta++;
    } else if(input[i]=="]"){
      beta--;
    }
  }
  if(alpha==0 && beta==0){
    func();
  } else {
    console.log(0)
  }
}
function func(){
  for(i=0; i<input.length; i++){
    if(input[i]=="("){
      asdf.push(2);
    } else if(input[i]=="["){
      asdf.push(3);
    } else if(input[i]==")"){
      asdf.push(-2);
    } else if(input[i]=="]"){
      asdf.push(-3);
    }
  }
}

for(i=0; i<asdf.length; i++){
  console.log(asdf[i])
}

///////포기
