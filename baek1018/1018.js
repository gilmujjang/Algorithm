const input = [
  '10',
  '13',
  'BBBBBBBBWBWBW',
  'BBBBBBBBBWBWB',
  'BBBBBBBBWBWBW',
  'BBBBBBBBBWBWB',
  'BBBBBBBBWBWBW',
  'BBBBBBBBBWBWB',
  'BBBBBBBBWBWBW',
  'BBBBBBBBBWBWB',
  'WWWWWWWWWWBWB',
  'WWWWWWWWWWBWB'
]

const file = input[0];
const row = input[1]; 

function case_w(input){
  let count = 0;
  for(i=2; i<input.length; i++){
    for(j=0; j<input[i].length; j++){
      if((i+j)%2==0){
        if(input[i][j]!='W'){
          count++;
        }
      } else {
        if(input[i][j]=='W'){
          count++;
        }
      }
    }
  }
  console.log(count);
}

function case_b(input){
  let count = 0;
  for(i=2; i<input.length; i++){
    for(j=0; j<input[i].length; j++){
      if((i+j)%2==0){
        if(input[i][j]!='B'){
          count++;
        }
      } else {
        if(input[i][j]=='B'){
          count++;
        }
      }
    }
  }
  console.log(count);
}

case_w(input);
case_b(input);

// 칠해야하는 칸의 개수를 구하는게 아니라 무슨 8*8 칸일때 최소라느니 훨씬더 복잡하다.
//모르겠다.