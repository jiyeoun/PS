n=int(input())
list_1=[0,1]
for i in range(2,n+1):
    list_1.append(list_1[i-1]+list_1[i-2])
print(list_1[n-1]+list_1[n-2])