function solution(s) {
    let answer = [];
    for (i=0; i<s.length; i++) {
        let distance = 0;
        for (j=i-1; j>=0; j--) {
            if (s[i] === s[j]) {
                distance = i-j;
                break;
            } 
        }
        answer[i] = distance===0 ? -1 : distance;
    }
    return answer
}
