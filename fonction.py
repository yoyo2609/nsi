from turtle import*
#ex 57

def test_pythagore(a,b,c):
    if a**2+b**2==c**2:
       return True
    else:
       return False

#ex 58
def valeur_absolue(a):
    if a<0:
       return 0-a
    else:
        return a
#ex60
def max2(a,b):
    if a>b:
        return a
    else:
        return b

#ex61
def max3(a,b,c):
    if a>b and a>c:
        return a
    elif b>a and a>c:
        return b
    else:
        return c
#ex68
def triangle(n):
    begin_fill()
    down()
    for i in range(3):
        forward(n)
        left(120)
    end_fill()

    
    

    