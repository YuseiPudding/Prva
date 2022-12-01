n=int(input("Unesi troznamenkasti cijeli broj: "))
if n>99 & n<1000:
  a=n%10
  n=n-a
  n=n//10
  b=n%10
  n=n-b
  n=n//10
  c=n%10
  print(a+b+c)
else:
  print("Nije unešen troznamenkasti broj.")
