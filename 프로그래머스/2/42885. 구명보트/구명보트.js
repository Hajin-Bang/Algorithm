function solution(people, limit) {
    let count = 0;
    let len = people.length;
    people.sort((a,b) => a-b);
    let start = 0;
    let end = len - 1;
    while (start<=end) {
        if (people[start] + people[end] <= limit) {
             start++;
            end--;
        } else {
            end--;
        }
        count++;
    }
    return count;
}