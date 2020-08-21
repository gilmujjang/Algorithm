/**
 * @param {number[]} nums
 * @return {number[]}
 */
var runningSum = function(nums) {
    let a = 0;
    let result = [];
    nums.forEach((x) => {
        a = a+x;
        result.push(a)
    })
    return result
};

/**
 * Runtime: 92 ms, faster than 26.52% of JavaScript online submissions for Running Sum of 1d Array.
 * Memory Usage: 37.1 MB, less than 28.40% of JavaScript online submissions for Running Sum of 1d Array.
 */