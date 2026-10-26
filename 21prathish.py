num =int(input("give the range of the prime find:"))

for n in range(1,num+1):
    if  n==2 :
        a=True
    elif n%2==0 or n==1:
        a=False
    else:

        for i in range(2,n):
            if n%i==0:
                a=False 
                break  
            else:    
                a=True     
    if a:
     print(n)
