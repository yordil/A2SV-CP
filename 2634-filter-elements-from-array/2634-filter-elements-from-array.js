/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */

var filter = function(arr, fn) {
    arrs = []
    
    for (let i = 0 ; i < arr.length ; i+=1){
         if (fn(arr[i], i)) 
            arrs.push(arr[i]);
    }
    
    return arrs
};