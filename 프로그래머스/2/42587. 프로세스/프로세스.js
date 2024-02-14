function solution(priorities, location) {
  let answer = 1;
  let realLocation = Array.from({ length: priorities.length }, (v, i) => i);
  while (priorities.length > 0) {
    if (priorities[0] === Math.max(...priorities)) {
      if (realLocation[0] === location) {
        return answer;
      } else {
        answer++;
        priorities.shift();
        realLocation.shift();
      }
    } else {
      priorities.push(priorities.shift()); 
      realLocation.push(realLocation.shift()); 
    }
  }
}