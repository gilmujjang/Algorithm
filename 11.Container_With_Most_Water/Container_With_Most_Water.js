/**
 * @param {number[]} height
 * @return {number}
 */
var maxArea = function(height) {
    const start = 0;
    const end = height.length;
    let arr1 = [];
    for(let i = 0; i< end; i++){
        let arr2 = [];
        for(let j = 0; j < end; j++){
            let h = Math.min(height[i],height[j]);
            let w = Math.abs(i-j);
            arr2.push(h*w)
        }
        arr1.push(Math.max(...arr2))
    }
    return Math.max(...arr1)
};

/**
 * Runtime: 8752 ms, faster than 5.03% of JavaScript online submissions for Container With Most Water.
 * Memory Usage: 70.2 MB, less than 5.00% of JavaScript online submissions for Container With Most Water.
 */

 /** 통과한 코드 중 최악의 코드 arr를 두개로 나눈 이유는 메모리 초과때문에 */