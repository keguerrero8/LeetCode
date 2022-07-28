/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var threeSumClosest = function(nums, target) {
    let res = Infinity
    let delta = Infinity
    nums.sort(function(a, b) {
        return a - b;
    })
    
    for (let i = 0; i < nums.length - 2; i++) {
        let l = i + 1
        let r = nums.length - 1
        while (l < r) {
            const currentSum = nums[i] + nums[l] + nums[r]
            const currentDelta = Math.abs(target - currentSum)
            if (currentDelta < delta) {
                res = currentSum
                delta = currentDelta
            }
            if (currentSum === target) {
                return res
            } else if (currentSum < target) {
                l += 1
            } else {
                r -= 1
            }  
        }
        
    }
    return res 
};