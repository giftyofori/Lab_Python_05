def prime(a):
     if divisor(a)==2:
         print a, "is a prime number"
     else:
         print a, "is not a prime number"

def divisor(a):
    count=0
    for i in range(1,a+1):
        if a%i==0:
            count +=1
    return count
