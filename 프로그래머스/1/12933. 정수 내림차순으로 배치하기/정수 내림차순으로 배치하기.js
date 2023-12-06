function solution(n) {
    n=String(n).split('').sort((a,b)=>b-a).join("");
    n=Number(n)
    return n;
}