change = int(input())

five_count = change // 5
while five_count >= 0:
    rest = change - (five_count * 5)
    if rest % 2 == 0:
        two_count = rest // 2
        print(five_count + two_count)
        break
    five_count -= 1
else:
    print(-1)
