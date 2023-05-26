/**
 * @param {Array} arr
 * @param {number} size
 * @return {Array[]}
 */
var chunk = function(arr, size) {
    let new_arr = []
    let count = 0

    let size_arr = []
    for (let val in arr) {
        count += 1
        size_arr.push(arr[val])
        if (count == size) {
            new_arr.push(size_arr)
            size_arr = []
            count = 0
        }else if (val == arr.length-1) {
            new_arr.push(size_arr)
        }
    }

    return new_arr
};