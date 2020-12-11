/**
 * @param {string} s
 * @return {string}
 */
var longestPalindrome = function(s) {
  let x = s.split("").join('.');
  let rightId=0;
  let centerId=0;
  let n = s.length;
  let radius = new Array(n).fill(0);
  for(let i=0; i<n; i++){
    if(i<=rightId){
      radius[i]=Math.min(radius[2*centerId-i],rightId-i);
    }
    while(0<i-radius[i]-1 && i+radius[i]<n && x[i-radius[i]-1]===x[i+radius[i]+1]){
      radius[i]++;
    }
    if(rightId<i+radius[i]){
      rightId=i+radius[i];
      centerId=i;
    }
  }
  let ans = [];
  let r = Math.max(...radius)
  let c = centerId/2;
  console.log(n)
  if(n%2==0){
    let c = centerId/2 +1;
    for(let i=c-r; i<=c+r-1; i++){
      ans.push(s[i])
    }
  } else {
    let c = centerId/2;
    for(let i=c-r; i<=c+r; i++){
      ans.push(s[i])
    }
  }
  return ans.join("");
};
/*
Wrong Answer
Details 
Input
"cbbd"
stdout
4

Output
""
Expected
"bb"

아직 해결 못함
*//