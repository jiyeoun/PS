while True:
    try:
        a=input()
        if a=='END':
            break
        print(a[::-1])
    except:
        break