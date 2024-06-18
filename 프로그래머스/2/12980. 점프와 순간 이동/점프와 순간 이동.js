function solution(n) {
    let answer = 0;
    while (n>0) {
        if (n % 2 === 1) {
            n = n - 1;
            answer++;
        } else n = n / 2;
    }
    return answer;
}