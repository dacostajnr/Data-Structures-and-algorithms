def isPalindrome(string):
    # reverse the string and check if it is the same as the original
    result=''
    for i in range(0,len(string)):
        result+=string[len(string)-1-i]
    if result==string:
        return True
    return False

print(isPalindrome("book"))
print(isPalindrome("noon"))
