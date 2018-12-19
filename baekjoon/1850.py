while True:
    try:
        a, b = input().split()
        a = int(a)
        b = int(b)

        def gcd(a, b):
            x = a % b
            while x > 0:
                a = b
                b = x
                x = a % b
            return b

        c = gcd(a, b)
        d = ""
        for i in range(c):
            d += "1"
        print(d)
    except:
        break