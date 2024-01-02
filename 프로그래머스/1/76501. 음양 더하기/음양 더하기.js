function solution(absolutes, signs) {
    let sum = 0;
    for (i=0; i<absolutes.length; i++) {
        if (signs[i] === true) {
            sum = sum + absolutes[i]
        } else if (signs[i] === false) {
            sum = sum - absolutes[i] 
        }
    }
    return sum;
}