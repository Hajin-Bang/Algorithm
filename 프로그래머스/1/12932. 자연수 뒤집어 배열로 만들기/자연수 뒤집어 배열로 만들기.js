function solution(n) {
    toString = String(n);
    array =toString.split('').reverse();
    answer = array.map(Number)
    return answer
}