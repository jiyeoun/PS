n=int(input())
fiv=0
thr=0
if n%3!=0 and n%5!=0 and n<8:
    print(-1)
else:
    if n%5==0:
        fiv=n//5
    elif n%5==1:
        fiv=n//5-1
        thr=2
    elif n%5==2:
        if n==7:
            fiv=-1
            thr=0
        elif n==12:
            fiv=0
            thr=4
        else:
            fiv=n//5-2
            thr=4
    elif n%5==3:
        fiv=n//5
        thr=1
    else:
        fiv=n//5-1
        thr=3
    print(thr+fiv)