n=int(input("Unesi bilo koji cijeli broj koji je manji od milijun: "))
if n<1000000:
    a=n%10
    n=n-a
    n=n//10
    b=n%10
    n=n-b
    n=n//10
    c=n%10
    n=n-c
    n=n//10
    d=n%10
    n=n-d
    n=n//10
    e=n%10
    n=n-e
    n=n//10
    f=n%10
    print(a+b+c+d+e+f)
else:
    print("Unešen je prevelik broj.")