a = int(input())
b = 64
count = 0

while a != 0:
    if b > a:
        b /= 2
    else:
        a -= b
        count += 1
print(count)