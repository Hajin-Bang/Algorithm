function solution(phone_book) {
  const hash = {};

  for (let phoneNumber of phone_book) {
    hash[phoneNumber] = true;
  }

  for (let phoneNumber of phone_book) {
    for (let i = 1; i<phoneNumber.length; i++) {
        let prefix = phoneNumber.substring(0,i);
        if(hash[prefix]) {
            return false;
        }
    }
  }
  return true;
}
