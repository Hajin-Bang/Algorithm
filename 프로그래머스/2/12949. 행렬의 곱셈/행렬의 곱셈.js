function solution(arr1, arr2) {
    const arr1Row = arr1.length;
    const arr1Column = arr1[0].length;
    const arr2Row = arr2.length;
    const arr2Column = arr2[0].length;
    
    const result = [];
    
    for (let i=0; i<arr1Row; i++) {
        result.push(new Array(arr2Column).fill(0))
    }
    
    for (let i=0; i<arr1Row; i++) {
        for (let j=0; j<arr2Column; j++)  {
            for (let k=0; k<arr1Column; k++) {
                result[i][j] += arr1[i][k] * arr2[k][j];
            }
        }
    }
    
    return result
}