import sys
input = sys.stdin.read().splitlines()

N = int(input[0])

files = {}
for i in range(1, N+1):
    file = input[i].split(".")
    extension = file[1]
    if (extension in files):
        files[extension] += 1
    else: files[extension] = 1

sorted_keys = sorted(files) # key를 사전순으로 정렬
for key in sorted_keys:
    print(f"{key} {files[key]}")