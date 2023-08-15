function solution(n) {
    let odd = [];
    for (i=0; i<=n; i++){
        if (i % 2 !== 0) {
            odd.push(i);
        }
    } return odd.sort((a,b) => a-b);
}