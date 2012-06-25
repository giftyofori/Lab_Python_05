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
    


    
        
        
        
