N = int(input())

files = {}
for _ in range(N):
    file = input().split(".")
    extension = file[1]
    if (extension in files):
        files[extension] += 1
    else: files[extension] = 1

sorted_keys = sorted(files) # key를 사전순으로 정렬
for key in sorted_keys:
    print(f"{key} {files[key]}")