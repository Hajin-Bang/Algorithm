function solution(s) {
    const lower_s = s.toLowerCase();
    let answer =   s.split(' ').map(word => 
    word.charAt(0).toUpperCase() + word.substring(1).toLowerCase()
  ).join(' ')
    return answer
    }
