n=int(input("Enter a number: "))

Mnum=1
Snum=0

for i in str(n):
    i=int(i)

    Mnum*=i
for i in str(n):
    i=int(i)

    Snum+=i


if Mnum == Snum:
    print("it is spy number")
else:
    print("it is not a spy number")    