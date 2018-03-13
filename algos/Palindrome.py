string=input()
length=len(string)
is_Palin=1
for i in range(length//2):
    if string[i]!=string[length-1-i]:
        print('not Palindrome')
        is_Palin=0
        break
if is_Palin:
    print('Palindrome')