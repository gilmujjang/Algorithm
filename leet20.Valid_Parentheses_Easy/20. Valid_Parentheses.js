/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function(s) {
  let a=[];
  if(s.length%2==0){
      for(let i=0; i<s.length; i++){
          let c = s[i];
          if(c=="("){
              a.push(1)
          }else if(c=="{"){
              a.push(2)
          }else if(c=="["){
              a.push(3)
          }else if(c==")" && a[a.length-1]===1){
              a.pop()
          }else if(c=="}" && a[a.length-1]===2){
              a.pop()
          }else if(c=="]" && a[a.length-1]===3){
              a.pop()
          }else{
              return false
          }
      }
  } else {
      return false
  }

  if(a.length==0){
      return true
  } else {
      return false
  }
}

/**
 * Runtime: 72 ms, faster than 86.85% of JavaScript online submissions for Valid Parentheses.
 * Memory Usage: 36.7 MB, less than 67.69% of JavaScript online submissions for Valid Parentheses.
 * 배열을 하나 만들어서 입력되는 기호에 따라 숫자를 추가했다가 닫는기호가 나오면 지워준다. 입력이 끝났을때 배열이 0 이면 통과
 */