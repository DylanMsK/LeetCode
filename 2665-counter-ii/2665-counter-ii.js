/**
 * @param {integer} init
 * @return { increment: Function, decrement: Function, reset: Function }
 */
var createCounter = function(init) {
    let now = init;
    return {
        increment: function() {
            now++;
            return now;
        },
        decrement: function() {
            now--;
            return now;
        },
        reset: function() {
            now = init
            return now;
        }
    }
};

/**
 * const counter = createCounter(5)
 * counter.increment(); // 6
 * counter.reset(); // 5
 * counter.decrement(); // 4
 */