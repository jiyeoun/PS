one=1
two=1
sum=0
n=int(input())
if n==1 or n==2:
    print(one)
else:
    for i in range(n-2):
        sum=one+two
        one=two
        two=sum
    print(sum)