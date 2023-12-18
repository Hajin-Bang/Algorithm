function solution(s){
    let pCounter=0;
    let yCounter=0;
    s = s.toUpperCase();
    for (let i=0; i<s.length; i++){
        if (s[i]==="P") {
            pCounter++;
        }
        if (s[i]==="Y") {
            yCounter++;
        }
    }
    return (pCounter === yCounter) ? true : false;
}