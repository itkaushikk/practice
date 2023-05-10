/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var filter = function(arr, fn) {
    let returnedArr = []

    //using i instead of parseInt(i) sends string type instead of integer
    for (let i in arr) {
        if (fn(arr[i], parseInt(i))) {
            returnedArr.push(arr[i])
        }
    }

    return returnedArr
    
};