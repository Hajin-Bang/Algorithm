function solution(progresses, speeds) {
    let answer = [];
    let leftDays = [];
    let prev = 0;
    for (let i=0; i<progresses.length; i++) {
        let leftDay = Math.ceil((100 - progresses[i]) / speeds[i]);
        leftDays.push(leftDay);
    }
    for(let i=0; i<leftDays.length; i++) {
        if(leftDays[prev] < leftDays[i]) {
            answer.push(i-prev);
            prev = i
        }
    }
    answer.push(leftDays.length-prev);
    return answer;
}
