n=int(input())
list_1=[]
sum=0
for i in range(n):
    a=int(input())
    if a==0:
        list_1.pop()
    else:
        list_1.append(a)
for j in range(len(list_1)):
    sum+=list_1[j]
print(sum)