input_value = input()
x, y, w, h = input_value.split()
x = int(x)
y = int(y)
w = int(w)
h = int(h)

distances = [x, y, w-x, h-y]
print(min(distances))