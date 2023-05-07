/**
 * @param {integer} init
 * @return { increment: Function, decrement: Function, reset: Function }
 */
var createCounter = function(init) {
    let given_number = init

    return {
        increment: function() {
            given_number += 1
            return given_number
        },
        decrement: function(){
            given_number -= 1
            return given_number
        },
        reset: function(){
            given_number = init
            return given_number
        }
    }
    
};

/**
 * const counter = createCounter(5)
 * counter.increment(); // 6
 * counter.reset(); // 5
 * counter.decrement(); // 4
 */