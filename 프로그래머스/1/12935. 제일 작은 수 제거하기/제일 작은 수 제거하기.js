function solution(arr) {
    let result = ''
    if (arr.length > 1) {
        result = arr.filter((x) => x !== Math.min(...arr))
        return result
    } else {
        return [-1];
    }
}