function solution(maps) {
    const n = maps.length;
    const m = maps[0].length;
    const dx = [-1, 0, 1, 0];
    const dy = [0, 1, 0, -1];
    
    const queue = [[0, 0]];
    const visited = Array.from(Array(n), () => Array(m).fill(false));
    visited[0][0] = true;
    
    const distance = Array.from(Array(n), () => Array(m).fill(0));
    distance[0][0] = 1;
    
    while (queue.length>0) {
        const [curX, curY] = queue.shift();
        for (let i=0; i<4; i++){
            const x = curX + dx[i];
            const y = curY + dy[i];
            
            if (x>=0 && x<n && y>=0 && y<m && maps[x][y]===1 && !visited[x][y]) {
                    queue.push([x,y]);
                    visited[x][y] = true;
                    distance[x][y] = distance[curX][curY] + 1; 
            }
        }
    }
    
    return distance[n-1][m-1] > 0 ? distance[n-1][m-1]:-1;
}