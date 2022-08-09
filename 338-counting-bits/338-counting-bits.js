/**
 * @param {number} n
 * @return {number[]}
 */
var countBits = function(n) {
    const arr = []
    for (let i = 0; i < n + 1; i++) {
        let num = i
        let count = 0
        while (num !== 0) {
            const rem = num % 2
            num = Math.floor(num/2)
            if (rem === 1) count++
        }
        arr.push(count)
    }
    
    return arr
};