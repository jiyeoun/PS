A,B=input().split()
A=int(A)
B=int(B)
C=int(input())
hour=0
min=0
if B+C>59:
	hour=(B+C)//60+A
	min=(B+C)%60
	if hour>23:
		hour=hour-24
		print(hour,min)
	else:
		print(hour,min)
		
else:
	print(A,B+C)