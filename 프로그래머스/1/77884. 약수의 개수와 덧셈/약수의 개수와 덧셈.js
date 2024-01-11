function solution(left, right) {
    let answer = 0;
    for (let i=left; i<=right; i++) {
        let result = Math.sqrt(i) % 1 === 0? -i : i;
        answer +=result;
    }
    return answer
}