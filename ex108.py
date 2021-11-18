from random import *
a=21
acc=0
print("il y a", a, "allumettes")
while a>0:
    n=int(input("combien en prenez vous?"))
    if n<1 or n>3:
        print("fuck you")
        break
    if n>a:
        print("fuck you")
        break
    a=a-n
    b=randint(1,3)
    if a ==2:
        b=randint(1,2)
    if a==1:
        b=1
    print("je prends", b, "alumettes")
    a=a-b
    print("il y a", a, "allumettes")
    if a==0:
        if acc%2==0:
            print("j'ai gagne")
        else: print("vous avez gagne")
        
