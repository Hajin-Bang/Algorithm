function solution(x) {
    let xString = x.toString().split('').map(Number);
    let sum = 0;
    for (let i=0; i<xString.length; i++) {
        sum += xString[i]
    }
    if (x % sum === 0) {
        return true
    } else return false
}