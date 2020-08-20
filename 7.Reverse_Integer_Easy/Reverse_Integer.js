/**
 * @param {number} x
 * @return {number}
 */
var reverse = function(x) {
    let b = x.toString().split("").reverse();
    if(b[0]==0){
      b.shift();
    }
    if(b[b.length-1]=="-"){
        b.pop();
        b.unshift("-")
    }
    const result =  Number(b.join(""));
    if(result>Math.pow(2,31)){
        return 0
    }
    else if(result<-Math.pow(2,31)){
        return 0
    }
    else{
        return result
    }
};

/**
 * Runtime: 84 ms, faster than 92.32% of JavaScript online submissions for Reverse Integer.
 * Memory Usage: 38.6 MB, less than 14.68% of JavaScript online submissions for Reverse Integer.
 */