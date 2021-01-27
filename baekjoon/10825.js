// let fs = require('fs');
// let input = fs.readFileSync('/dev/stdin').toString().split('\n');

const input = [
  '12',
  'Junkyu 50 60 100',
  'Sangkeun 80 70 100',
  'Sunyoung 80 70 100',
  'Soong 50 60 90',
  'Haebin 50 60 100',
  'Kangsoo 60 80 100',
  'Donghyuk 80 60 100',
  'Sei 70 70 70',
  'Wonseob 70 70 90',
  'Sanghyun 70 70 80',
  'nsj 80 80 80',
  'Taewhan 50 60 90'
]

let ans = [];
const size = Number(input[0])+1;

for(i=1; i<size; i++){
  let a = input[i].toString().split(' ');
  ans.push(a);
}

// ans.sort((a,b) => {
//   if(a[1]==b[1]){
//     if(a[2]==b[2]){
//       if(a[3]==b[3]){
//         return b[0]-a[0]   ///국영수 다 같으면 이름순
//       } else {
//         return a[3]-b[3]   ///국영만 같으면 수학 내림차순
//       }
//     } else {   ///국만 같으면 영어 오름차순
//       return b[2]-a[2]
//     }
//   } else {  //국어점수 다르면 내림차순
//     return a[1]-b[1]
//   }
//   return b[1]-a[1]
// })

ans.sort((a,b) => {
  if(a[1]==b[1]){
    if(a[2]==b[2]){
      if(a[3]==b[3]){
        return a[0]<b[0] ? -1 : a[0]>b[0] ? 1 : 0; //국영수 같을때
      } else {
        return a[3]<b[3] ? -1 : a[3]>b[3] ? 1 : 0;   //국영 같을때
      }
    } else {
      return a[2]<b[2] ? -1 : a[2]>b[2] ? 1 : 0;  //국만 같을때
    }
  } else {
    return b[1]-a[1]
  }
})

for(i=0; i<ans.length; i++){
  console.log(ans[i][0])
}
