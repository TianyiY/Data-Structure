# helper function to judge whether it is palindromes or not
def isPalindromes(string):
    if string==string[::-1]:
        return True
    return False

# function returen the longest palindromes
def palindromes(string):
    length=len(string)
    res=[]
    for n in range(length):
        for m in range(n):
            substring=string[m:n+1]          # traverse all the combinations
            if isPalindromes(substring):
                temp=substring     # if true, give the value to palindromes
                res.append(temp)
    if len(res)>0:
        return res
    else:
        return 'Sorry, no palindromes found'

# test
print palindromes('grabcddcbarg')


