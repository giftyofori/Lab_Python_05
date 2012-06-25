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

