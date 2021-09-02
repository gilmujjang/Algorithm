// 이게 도대체 왜 틀린건지 모르겠네

const input = [
  '15',
  'push 1',
  'push 2',
  'front',
  'back',
  'size',
  'empty',
  'pop',
  'pop',
  'pop',
  'size',
  'empty',
  'pop',
  'push 3',
  'empty',
  'front'
]
let num = [];

for(i=1; i<input.length; i++){
  const now = input[i];
  const s = num.length;
  switch(now){
    case 'pop':
      if(s>0){
        console.log(num[0]);
        num.splice(0,1);
      } else {
        console.log(-1)
      }
      break;

    case 'size':
      console.log(s);
      break;

    case 'empty':
      if(s>0){
        console.log(0)
      } else {
        console.log(1)
      }
      break;

    case 'front':
      if(s>0){
        console.log(num[0]);
      } else {
        console.log(-1)
      }
      break;

    case 'back':
      if(s>0){
        console.log(num[s-1]);
      } else {
        console.log(-1);
      }
      break;

    default:
      const [n, ne] = now.split(' ')
      num.push(ne);
      break;
  }
}