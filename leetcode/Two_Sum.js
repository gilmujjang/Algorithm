/** 
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
*/


var twoSum = function(nums, target) {
  const indices = new Map();
  const result = [];
  
  for(let i = 0; i < nums.length; i++) {
      const num = nums[i];
      const complement = target - num;
      
      if(indices.has(complement)){
          result[0] = indices.get(complement);
          result[1] = i;
          
          return result;
      }
      indices.set(num,i);
  }
};

/**
 * Runtime: 76 ms, faster than 79.91% of JavaScript online submissions for Two Sum.
 * Memory Usage: 38.2 MB, less than 10.81% of JavaScript online submissions for Two Sum.
*/