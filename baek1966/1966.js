//let fs = require('fs');
//let input = fs.readFileSync('/dev/stdin').toString().split('\n');

const input = [
  '4',
  '3', '0',
  '5', '1', '2',
  '4', '2',
  '1', '2', '3', '4',
  '6', '0',
  '1', '1', '9', '1', '1', '1',
  '5', '1',
  '1', '3', '4', '2', '9'
]


let id = 0;
let size = 0;
  
for(i=1; i<input.length; i){
  let id = input[i+1];
  let size = input[i];
  let content = [];
  let index = [];
  i = i +2;
  for(j=0; j<size; j++){
    content.push(parseInt(input[i]));
    if(j==id){
      index.push(1);
    } else {
      index.push(0);
    }
    i++;
  }
  for(j=0; j<size; j++){
    if()
  }
  console.log(content);
  console.log(index);
}

//아 모르겠다
// 이제 내림차순으로 정렬해야 하는데 index 도 저런식으로 넣으면 안될것같고
// 하기싫다