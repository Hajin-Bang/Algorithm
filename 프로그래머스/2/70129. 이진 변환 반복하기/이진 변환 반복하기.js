function solution(s) {
    let count = 0;
    let zeroCount = 0;

    while (s !== '1') {
        let length = s.length;
        s = s.replace(/0/g, '');  
        zeroCount += (length - s.length);  
        s = s.length.toString(2);  
        count++;  
    }

    return [count, zeroCount];
}