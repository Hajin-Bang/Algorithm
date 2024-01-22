function solution(clothes) {
  const clothesMap = {};
  for (let i = 0; i < clothes.length; i++) {
    let type = clothes[i][1];

    if (!clothesMap[type]) {
      clothesMap[type] = 1;
    } else {
      clothesMap[type]++;
    }
  }

  let answer = 1;
  for (let type in clothesMap) {
    answer *= clothesMap[type] + 1;
  }

  return answer - 1;
}