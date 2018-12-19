n=int(input())
list_1=[]
for i in range(n):
    list_1.append(int(input()))
list_1=sorted(list_1)
for j in range(n):
    print(list_1[j])