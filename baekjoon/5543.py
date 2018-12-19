list_1=[]
list_2=[]
for i in range(3):
    a=int(input())
    list_1.append(a)
for j in range(2):
    b=int(input())
    list_2.append(b)
print(min(list_1)+min(list_2)-50)