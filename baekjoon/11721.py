a=str(input())
len_a=len(a)
sum=0
if len_a %10 != 0:
    sum= len_a//10+1
else:
    sum=len_a//10

for i in range(sum):
    print(a[i*10:(i+1)*10])