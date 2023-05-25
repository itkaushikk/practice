/**
 * @param {any} o1
 * @param {any} o2
 * @return {boolean}
 */
var areDeeplyEqual = function(o1, o2) {
    let are_deeply_equal = true

    if (Array.isArray(o1) || Array.isArray(o2)) {

        if (Array.isArray(o1) != Array.isArray(o2)) {
            return false
        }

        if (o1.length != o2.length) {
            return false
        }

        let deep_check = false
        if (typeof(o1[0]) == "object" && o1.length == 1) {
            deep_check = areDeeplyEqual(o1[0], o2[0])
            return deep_check
        }

        for (let val in o1) {
            deep_check = areDeeplyEqual(o1[val], o2[val])
        }
        
        if (deep_check) {
            return deep_check
        }
        return JSON.stringify(o2) == JSON.stringify(o1)
    }

    if (typeof(o1) == "number" || typeof(o2) == "number") {
        return JSON.stringify(o1) == JSON.stringify(o2)
    }

    if (typeof(o1) == "string") {
        return JSON.stringify(o1) == JSON.stringify(o2)
    }

    if (typeof(o1) == "boolean") {
        if (o1 !== o2) {
            return false
        }
    }

    for (let val in o1) {
        console.log(val)
        if (JSON.stringify(o2[val]) != JSON.stringify(o1[val])) {
            let deep_check = false
            if (Array.isArray(o1[val])) {
                deep_check = areDeeplyEqual(o1[val], o2[val])
            }
            if (typeof(o2[val]) == "object") {
                deep_check = areDeeplyEqual(o2[val], o1[val])
            }
            if (deep_check) {
                return true
            } 
            are_deeply_equal = false
            return are_deeply_equal
        }
    }

    return are_deeply_equal
    
};