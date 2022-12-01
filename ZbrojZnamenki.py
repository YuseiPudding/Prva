n=int(input("Unesi troznamenkasti cijeli broj: "))
a=n%10
n=n-a
n=n//10
b=n%10
n=n-b
n=n//10
c=n%10
print(a+b+c)