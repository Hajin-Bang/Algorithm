function solution(hp) {
    let ant = 0; 
    ant = Math.floor(hp / 5);
    ant += Math.floor((hp % 5) / 3);
    ant += Math.floor((hp % 5) % 3);
    
    return ant;
}


