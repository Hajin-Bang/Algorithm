function count(n) {
    let binary = n.toString(2);
    let countOne = 0; 
    for (let i=0; i<binary.length; i++) {
        if(binary[i] == '1') {
            countOne ++;
        }
    }
    return countOne;
}


function solution(n) {
    let testNum = n;
    while (true) {
        testNum++;
        if (count(testNum) == count(n)) return testNum;
    }
}