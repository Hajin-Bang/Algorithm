function solution(a, b) {
    let answer = 0;
        if (a<b) {
            for (i=a; i<=b; i++) {
                answer += i
            } 
        } else if (a>b) {
            for (i=b; i<=a; i++) {
                answer += i
            }
        } else answer = a
    return answer
    }