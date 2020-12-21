//let fs = require('fs');
//let input = fs.readFileSync('/dev/stdin').toString().split('\n');

const input = [
'121',
'1231',
'12421',
'12345654321',
'1234553421',
'0'
]

// for(i=0; i<input.length-1; i++){
//   let q = input[i];
//   let p = q.length;
//   let bo = true;
//   let j = 0;

//   while(j<p/2){
//     if(q[j]!=q[p-1-j]){
//       bo = false;
//       break;
//     }
//     j++;
//   }
//   if(bo){
//     console.log("yes");
//   } else {
//     console.log("no");
//   }
// }

// 맞는데 왜 틀리다는겨;;
for(i=0; i<input.length-1; i++){
  if(input[i]==input[i].split("").reverse().join("")){
    console.log("yes");
  } else {
    console.log("no");
  }
}
