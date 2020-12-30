// let fs = require('fs');
// let inpu = fs.readFileSync('/dev/stdin').toString().split('\n');
// let input = []
// for(i=0; i<inpu.length; i++){
//     let a = inpu[i].toString().split(' ')
//     for(j=0; j<a.length; j++){
//         input.push(a[j])
//     }
// }

const input = [
  '3',
  '1', '0',
  '5',
  '4', '2',
  '1', '2', '3', '4',
  '6', '0',
  '1', '1', '9', '1', '1', '1'
]

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
  let t = 1;

  for(j=0; j<size*size; j++){

    if(content[0]==Math.max(...content)){
      if(index[0]==1){
        console.log(t)
        break
      } else {
        content.shift()
        index.shift()
        t++;
      }
    } else {
      content.push(content.shift())
      index.push(index.shift())
    }
  }
}