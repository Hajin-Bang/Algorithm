function solution(array, commands) {
    let answer = [];
    for (let a=0; a<commands.length; a++) {
        let i = commands[a][0];
        let j = commands[a][1];
        let k = commands[a][2];
        
        let newArr = array.slice(i-1,j).sort((a,b) => a-b);
        answer.push(newArr[k-1])
    }    
    return answer;
}      