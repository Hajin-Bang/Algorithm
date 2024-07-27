function solution(n) {
    let a = 1;
    let b = 1; 
    let answer = 1;
    
    for (let i=2; i<n+1; i++) {
        answer = (a + b) % 1234567;
        a = b;
        b = answer;
    }
    return n === 1 ? 1 : answer;
}