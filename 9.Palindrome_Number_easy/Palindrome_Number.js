/**
 * @param {number} x
 * @return {boolean}
 */
var isPalindrome = function(x) {
  if(x<0) {
      return false
  }
  
  let b = x.toString().split('').reverse().join('');
  if( b==x ){
      return true
  } else {
      return false
  }
}

/**
 * Runtime: 252 ms, faster than 44.31% of JavaScript online submissions for Palindrome Number.
 * Memory Usage: 47 MB, less than 20.96% of JavaScript online submissions for Palindrome Number.
 */