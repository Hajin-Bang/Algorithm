function solution(N, stages) {
    let failed = [];
    
    for (let i=1; i<=N; i++) {
        let notClear = stages.filter(stage => stage === i).length;
        let reach  = stages.filter(stage => stage >= i).length;
        let failureRate = notClear / reach;
        
        failed.push({ stage: i, rate: failureRate });
    }
    failed.sort((a, b) => b.rate - a.rate);
    return failed.map(obj => obj.stage);
}