function solution(participant, completion) {
    const participantMap = new Map();
    // 'participant' 배열의 각 요소를 key로 하고, 해당 요소의 출현 횟수를 value로 하는 해시맵
    
    // 참가자 목록을 해시맵에 추가
    for (let name of participant) {
        // participant 배열의 각 요소를 순회하면서 'name' 변수에 할당한다
        participantMap.set(name, (participantMap.get(name) || 0) + 1);
        // name이 있을 때: 그 값을 반환한 뒤 + 1
        // name이 없을 때: 0을 반환한 뒤 + 1
    }
                           
    // 완주자 목록에서 참가자를 제외
    for (let name of completion) {
        participantMap.set(name, participantMap.get(name) - 1);
        if (participantMap.get(name) === 0) {
            participantMap.delete(name);
        } // 1씩 감소한 결과 인원수가 0이 되었다면, 해당 참가자를 해시맵에서 삭제
    }
        
    // 해시맵에 남아있는 참가자 확인
    const answer = [...participantMap.keys()][0];
    return answer;
}