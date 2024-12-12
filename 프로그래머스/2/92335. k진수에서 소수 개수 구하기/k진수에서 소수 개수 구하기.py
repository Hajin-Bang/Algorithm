'''
437674 3진수
211020101011

211
2
11

437674 3진수
'''
import math

def is_correct(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def solution(n, k):
    k_num = ''
    while n > 0:
        k_num = str(n % k) + k_num
        n //= k
    
    numbers = k_num.split('0')
    
    result = 0
    for num in numbers:
        if num and is_correct(int(num)):
            result += 1
    
    return result


'''
numbers = ["211","2","1","1","11"]

'''