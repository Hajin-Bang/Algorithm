def recursion(s, l, r):
    global recursionCount
    recursionCount += 1
    if (l >= r):
        return 1
    elif (s[l] != s[r]):
        return 0
    else:
        return recursion(s, l+1, r-1)

def isPalindrome(s):
    return recursion(s, 0, len(s)-1 )

testCase = int(input())

for i in range(testCase):
    recursionCount = 0
    s = input()
    print(isPalindrome(s), recursionCount)