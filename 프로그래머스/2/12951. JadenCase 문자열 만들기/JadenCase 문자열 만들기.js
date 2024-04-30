function solution(s) {
    sList = s.split(" ");
    let answer = [];
    
    for (let word of sList) {
        word = word.charAt(0).toUpperCase() + word.slice(1).toLowerCase();
        answer.push(word);
    }
    
    
    return answer.join(" ");
}