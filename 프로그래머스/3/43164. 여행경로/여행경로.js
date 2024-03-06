function solution(tickets) {
    let queue = [];
    function dfs(extra, current, route) {
        if(extra.length===0) {
            queue.push(route);
        }
        else {
            extra.forEach(([start,end], index) => {
                if (current ===start) {
                    const newExtra = extra.slice();
                    newExtra.splice(index,1); 
                    
                    dfs(newExtra, end, route.concat(end));
                }
            });
        }
    };
    dfs(tickets, 'ICN', ['ICN']);
    return queue.sort()[0];
}