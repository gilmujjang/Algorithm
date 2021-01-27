// const fs = require('fs');
// const input1 = fs.readFileSync('/dev/stdin').toString();
//const input = input[0];

const input = "baekjoon";
let ans = [];
let data = [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1];
for(i=0; i<input.length; i++){
    asci = input.charCodeAt(i)-97;
    data[asci]=i;
};
for(i=0; i<data.length; i++){
    ans.push(data[i])
}
console.log(ans.join(''))
///맞는데 백준에서는 왜 런타임에러가 나는지 모르겠음