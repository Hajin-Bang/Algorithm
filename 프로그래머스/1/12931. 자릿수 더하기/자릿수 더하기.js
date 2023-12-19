function solution(n)
{
    var answer = 0;
    let N = String(n);
    for (i=0; i<N.length; i++) {
        answer += parseInt(N[i]);
    }
    return answer;
}