#ex94
n=1
np=0
while n<1000:
	N=n
	n=np+n
	np=N
	print(np)
#ex68

from turtle import*

def triangle(n):
	begin_fill()
	for i in range(3):
		forward(n)
		left(120)
	end_fill()

triangle(100)
	

	
	
