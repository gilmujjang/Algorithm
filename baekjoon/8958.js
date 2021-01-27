
 
// const fs = require('fs');
// const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

const input = [
  '5',
  'OOXXOXXOOO',
  'OOXXOOXXOO',
  'OXOXOXOXOXOXOX',
  'OOOOOOOOOO',
  'OOOOXOOOOXOOOOX'
];
for(i=1; i<input.length; i++){
  let x = 0;
  let ans = 0;
  for(j=0; j<input[i].length; j++){
    if(input[i][j] == "O"){
      x = x+1;
      ans = ans + x;
    } else {
      x = 0;
    }
  }
  console.log(ans);
}
