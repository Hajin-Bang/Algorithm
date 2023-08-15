function solution(n) {
    let pair = [];
    for (i=1; i<=n; i++){
        if (n % i === 0) {
        pair.push(i);
        pair.push(parseInt(n/i));
        }
    }
    return pair.length / 2;
}