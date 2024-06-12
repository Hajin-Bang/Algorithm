function solution(brown, yellow) {
    for (let i = 1; i <= Math.sqrt(yellow); i++) {
        if (yellow % i === 0) {
            let width = yellow / i;
            let length = i;
            if ((width + 2) * (length + 2) === brown + yellow) {
                return [width + 2, length + 2];
            }
        }
    }
}