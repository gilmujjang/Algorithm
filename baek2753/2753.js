// const fs = require('fs');
// const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

input = 2000;

if(input % 4 ==0 ){
  if(input%100==0){
    if(input%400==0){
      console.log(1);
    } else{console.log(0);}
  } else {console.log(1);}
} else {console.log(0);}