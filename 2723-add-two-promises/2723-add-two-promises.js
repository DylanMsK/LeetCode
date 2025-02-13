/**
 * @param {Promise} promise1
 * @param {Promise} promise2
 * @return {Promise}
 */
// var addTwoPromises = async function(promise1, promise2) {
//     return new Promise((resolve, reject) => {
//         Promise.all([promise1, promise2]).then((values) => {
//             resolve(values[0] + values[1]);
//         });
//     });
// };
var addTwoPromises = async function(...args) {
    return new Promise((resolve, reject) => {
        Promise.all(args).then((values) => {
            resolve(values.reduce((a, b) => a + b, 0));
        });
    });
};

/**
 * addTwoPromises(Promise.resolve(2), Promise.resolve(2))
 *   .then(console.log); // 4
 */