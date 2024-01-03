function solution(arr, divisor) {
    let answer = [];
    let noAnswer = [-1];
    for (i=0; i<arr.length; i++) {
        if (arr[i] % divisor === 0) {
            answer.push(arr[i]);
        } 
    }
    answer.sort((a,b) => a-b)
    return answer.length !== 0 ? answer : noAnswer
}