name=input()
sum=[name[0]]
for i in range(len(name)):
    if name[i]=='-':
        sum.append(name[i+1])
for i in range(len(sum)):
    print(sum[i],end='')
print()