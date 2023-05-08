/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var map = function(arr, fn) {
    let returnedArray = []

    for (let i in arr) {
        returnedArray[i] = fn(parseInt(arr[i]), parseInt(i))
    }
    
    return returnedArray
};