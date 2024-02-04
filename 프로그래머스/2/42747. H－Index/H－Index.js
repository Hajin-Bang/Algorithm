function solution(citations) {
    let answer = 0;
    for (let i=citations.length; i>=1; i--) {
        if (citations.filter(num => num>=i).length >= i) {
            answer = i
            break;
        }
    }  
    return answer
}
    
