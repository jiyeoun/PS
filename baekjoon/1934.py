def gcd(a, b):
    while b != 0:
        x = a % b
        a = b
        b = x
    return a


def lcm(a, b):
    gcd2 = gcd(a, b)
    return (a * b) // gcd2

n=int(input())
for i in range(n):
    a,b=input().split()
    a=int(a)
    b=int(b)
    print(lcm(a, b))
