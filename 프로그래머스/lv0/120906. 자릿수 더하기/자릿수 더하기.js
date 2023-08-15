function solution(n) {
    n = n.toString().split("");
    n = n.map(Number);
    const sum = n.reduce((acc, cur) => acc+cur, 0);
    return sum;
}