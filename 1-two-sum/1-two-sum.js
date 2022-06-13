/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */

//{2:0, }
var twoSum = function(nums, target) {
    const valueMap = {}
    for (let i = 0; i < nums.length; i++) {
        delta = target - nums[i] 
        if (delta in valueMap) {
            return [i, valueMap[delta]]
        }
        else {
            valueMap[nums[i]] = i
        }
    }
    
};