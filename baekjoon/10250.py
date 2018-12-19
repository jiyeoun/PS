a=int(input())
for i in range(a):
    H, W, N = input().split()
    H = int(H)
    N = int(N)
    bot=1
    top=1

    if H==1:
        top=1
        bot=N
    else:
        while N>1:
            N-=1
            top+=1
            if top>H:
                top=1
                bot+=1

    if bot<10:
        top=str(top)
        bot=str(bot)
        print(top+'0'+bot)
    else:
        top=str(top)
        bot=str(bot)
        print(top+bot)