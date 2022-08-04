/**
 * Encodes a list of strings to a single string.
 *
 * @param {string[]} strs
 * @return {string}
 */
var encode = function(strs) {
    if (strs === "") return ""
    const res = []
    for (const word of strs) {
        res.push(word.length.toString(), "#")
        for (const letter of word) {
            res.push(letter)
        } 
    }
    return res.join("")
};

/**
 * Decodes a single string to a list of strings.
 *
 * @param {string} s
 * @return {string[]}
 */
var decode = function(s) {
    if (s === "") return [""]
    const res = []
    let i = 0
    while (i < s.length) {
        const j = i
        while (s[i] !== "#") {
            i++
        }
        const count = parseInt(s.slice(j, i))
        i += 1
        res.push(s.slice(i, i + count))
        i += count 
    }
    return res
};

/**
 * Your functions will be called as such:
 * decode(encode(strs));
 */