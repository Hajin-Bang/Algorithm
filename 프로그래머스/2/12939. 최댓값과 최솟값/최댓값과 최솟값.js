function solution(s) {
    let answer = "";
    let arr = s.split(" ");
    let max = Math.max(...arr);
    let min = Math.min(...arr);
    
    answer = min + " " + max;
    
    return answer;
}