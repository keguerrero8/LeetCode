/**
 * @param {number[]} nums1
 * @param {number} m
 * @param {number[]} nums2
 * @param {number} n
 * @return {void} Do not return anything, modify nums1 in-place instead.
 */
var merge = function(nums1, m, nums2, n) {
    if (n === 0) return nums1
    let n1 = nums1.length - n - 1
    let n1Zero = nums1.length - 1
    let n2 = nums2.length - 1
    
    while (n1 >= 0 && n2 >= 0) {
        if (nums2[n2] > nums1[n1]) {
            nums1[n1Zero] = nums2[n2]
            n2--
        } else {
            nums1[n1Zero] = nums1[n1]
            n1--
        }
        n1Zero--
    }
    while (n2 >= 0) {
        nums1[n1Zero] = nums2[n2]
        n2--
        n1Zero--
    }
    
    return nums1
};