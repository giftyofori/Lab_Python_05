def facto(a):
    b=1
    for c in range(1,a+1):
        b=b*c
    return b
   

def do(thing):
    return str(thing)+str(1)
#this function accepts a single parameter, turns it into string and adds another string '1 tom it'



#b.
def do(one, two=5):
      return one +two
# this function accepts a number and adds 5 to it

# c.
def do(a,b):
    return a*b
inp=8
do(inp,5)
print inp
# 8


#d

def try_to_change_list_content(the_list):
    the_list.append('four')
outer_list=['one','two','three']
try_to_change_list_content(outer_list)
print outer_list

#this prints  ['one','two', 'three', 'four']

#e
def do(a,f):
    return a*f(a)
def inp(a):
    return a*2
print do(6,inp)

# 72

def fibo(c):
    first_num=1
    next_num=0
    result=0
    newresult=[]

    for a in range(0,c+1): #first result is value of firstnumber plus next number
        result=first_num+next_num
        first_num=next_num #now first number takes value of next number
        next_num=result #next number now takes the value of result
        newresult.append(result)
    return newresult



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

