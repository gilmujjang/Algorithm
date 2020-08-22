/**
 * @param {string[]} strs
 * @return {string}
 */
var longestCommonPrefix = function(strs) {
    let result = []
    let container = strs[0];
    strs.forEach(element => {
        result = [];
        for( let i = 0; i < Math.min(element.length, container.length); i++){
            if(container[i] == element[i]) {
                result.push(element[i]);
            } else {
                break;
            }
        }
        container = result;
    });
    return result.join("")
};

/**
 * Runtime: 88 ms, faster than 45.92% of JavaScript online submissions for Longest Common Prefix.
 * Memory Usage: 38.7 MB, less than 17.82% of JavaScript online submissions for Longest Common Prefix.
 */