a = int(input("longueur a:"))
b = int(input("longueur b:"))
c = int(input("longueur c:"))
if c<a+b:
    if a==b==c:
        print("le triangle est equilateral")
    elif a==b or b==c or a==c:
        print("le triangle est isocele")
    else:
        print("le triangle est scalene")
else:
    print("triangle impossible")