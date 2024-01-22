function solution(phone_book) {
    const phoneDict = {}
    
    phone_book.forEach(phoneNumber => {
        phoneDict[phoneNumber] = true
    })

    for(const phoneNumber of phone_book) {
        for(let i = 1 ; i < phoneNumber.length ; i ++) {
            const curStr = phoneNumber.slice(0, i)
            if(phoneDict[curStr]) return false
        }
    }
    
    return true
}