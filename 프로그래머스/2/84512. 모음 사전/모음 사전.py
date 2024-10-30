# 단어 짧은 것부터 ~ 긴 순서대로 나열 
# 단어 길이가 같다면 
    # 글자 순서대로 나열 AA AE AI AO AU
    
# 모든 단어를 사전식으로 정렬 (재귀함수로 리스트 생성)
# 해당 단어의 위치를 찾는다


def solution(word):
    vowels = ["A", "E", "I", "O", "U"] 
    words = [] # 단어를 저장할 리스트

    def generate(current_word):
        if len(current_word) > 5:
            return
        words.append(current_word) 
        for vowel in vowels:
            generate(current_word + vowel) # AA AE AI AO AU

    generate("") # A 

    return words.index(word)