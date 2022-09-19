/**
 * @param {number} numRows
 * @return {number[][]}
 */
var generate = function(numRows) {
    if (numRows === 1) return [[1]]
    
    const res = [[1]]
    let i = 1
    
    while (i < numRows) {
        const parent = res[res.length - 1]
        const nextLayer = []
        
        for (let j = 0; j < parent.length; j++) {
            const leftB = j > 0? parent[j-1] : 0
            nextLayer.push(parent[j] + leftB)
        }
        
        nextLayer.push(1)
        res.push(nextLayer)
        i++
    }
    
    return res
    
};