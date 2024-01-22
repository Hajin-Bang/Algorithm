function solution(nums) {
    let answer = 0;
    let choice = Math.floor(nums.length/2);
    let Length = [...new Set(nums)].length
    
    return Length < choice ? Length : choice;
}