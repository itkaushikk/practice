Array.prototype.last = function() {
    let last_index = this.length-1
    let last_val = this[last_index]

    if (this.length == 0) {
        last_val = -1
    }

    return last_val
    
};

/**
 * const arr = [1, 2, 3];
 * arr.last(); // 3
 */