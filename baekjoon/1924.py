mon,day=input().split()
mon=int(mon)
day=int(day)
total_mon=0

list_1=[31,28,31,30,31,30,31,31,30,31,30,31]
list_2=['SUN','MON','TUE','WED','THU','FRI','SAT']

for i in range(0,mon-1):
    total_mon+=list_1[i]

total_day=total_mon+day

for i in range(7):
    if total_day%7==i:
        print(list_2[i])