function solution(n) {
    for(i=1; i*i<=n; i++) {
        if(i*i == n) {
            answer = (i+1)*(i+1)
        } else answer = -1
    } 
    return answer
}