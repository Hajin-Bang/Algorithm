function solution(num) {
    let i = 0;
    if (num === 1) {return 0}
    while (num !== 1) {
        if (num % 2 === 0) {
            num = num/2;
        } else {
            num = num*3 + 1;
        }
        i += 1;
    } 
    if (i < 500) {
        return i
    } else if ( i => 500 ) {
        return -1
    }
}