/**
 * @param {string} digits
 * @return {string[]}
 */
var letterCombinations = function(digits) {
  let result = [];
  const number = [[],[],["a","b","c"],["d","e","f"],["g","h","i"],
             ["j","k","l"],["m","n","o"],["p","q","r","s"],
             ["t","u","v"],["w","x","y","z"]];
  for(let i=0; i<number[digits[0]].length; i++){
      for(let j=0; j<number[digits[1]].length; j++){
          result.push(number[digits[0]][i] + number[digits[1]][j])
      }
  }

  return result
};


/**
 * TypeError: Cannot read property 'length' of undefined
 * 이거말고도 forEach를 쓰려했는데 그것도 같은 에러가 났다. 
 * 일단 통과한 다음에 리팩토링하려고 막 짰는데 에러가 난다. Run Code는 통과하는데 Submit 하면 에라가난다
 * 다른 사람들 제출한거 보면 신기하게 짧게 잘한다.
 */