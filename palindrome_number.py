def isPalindrom(n):
    num=n
    rev=0
    while (n>0):
        # get the last number
        d=n%10
        # cut off number for the net round
        n=n//10
        # update reverse
        rev=d+rev*10
    if rev==num:
        return  True
    return False

print(isPalindrom(141))
print(isPalindrom(121121))
print(isPalindrom(1411))
        
