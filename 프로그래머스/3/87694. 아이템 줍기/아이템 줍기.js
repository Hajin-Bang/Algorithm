function solution(rectangle, characterX, characterY, itemX, itemY) {
    characterX *=2;
    characterY *=2;
    itemX*=2;
    itemY*=2;
    
    let doubleRec = rectangle.map(rec => rec.map (point => point*2));

    const dx=[0,0,-1,1];
    const dy=[-1,1,0,0];
    
    let map = Array.from({length:103},() => Array(103).fill(0));

    
    doubleRec.forEach(([x1,y1,x2,y2])=>{
        
        for(let i=x1;i<=x2;i++){
            for(let j=y1;j<=y2;j++){
                if(i === x1 || i === x2 || j === y1 || j === y2){
                    if(map[i][j]===0){map[i][j]=1;}
                }
                else{map[i][j]=2;}
            }
        }
        
    });
    
    let start=[characterX,characterY,0];
    let queue = [start];

    map[characterX][characterY]=0;
    
    while(queue.length > 0){
        
        let [x,y,cnt]=queue.shift();
        
        
        if(x === itemX && y === itemY){ return cnt/2; }
        
        for(let d=0;d<4;d++){
            let nx=x+dx[d];
            let ny=y+dy[d];
            if(map[nx][ny]===1){
                queue.push([nx,ny,cnt+1]);
                map[nx][ny]=0;
            }
        }
        
    }
    
    return 0;
}