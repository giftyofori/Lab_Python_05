def isPalindrome(something):
    b=''
    for c in something:
         b=c+b
    if b==something:
        return True
    else:
        return False
        
        
    
