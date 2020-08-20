/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number}
 */
var findMedianSortedArrays = function(nums1, nums2) {
  let arr = nums1.concat(nums2);
  arr.sort((a,b) => a-b);
  const x = arr.length;
  if(x%2==0){
      return ((arr[x/2 -1]+arr[x/2])/2)
  } else {
      return (arr[x/2 -0.5])
  }
};

/**
 * Runtime: 128 ms, faster than 83.72% of JavaScript online submissions for Median of Two Sorted Arrays.
 * Memory Usage: 41.8 MB, less than 76.63% of JavaScript online submissions for Median of Two Sorted Arrays.
 */