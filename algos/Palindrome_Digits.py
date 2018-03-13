ten_base = 11
two_base = bin(ten_base)
eight_base = oct(ten_base)
print(str(ten_base))
print(str(two_base))
print(str(eight_base))

order = 12345
reversed_order = str(order)[::-1]
print(reversed_order)

def is_All_Palindrome_digits(number):
    ten_base = str(number)
    two_base = str(bin(number))[2:]       # get rid of the first two strings '0b'
    eight_base = str(oct(number))[2:]     # get rid of the first two strings '0o'
    if ten_base == ten_base[::-1] and two_base == two_base[::-1] and eight_base == eight_base[::-1]:
        print("Ten Base Digits："+ten_base)
        print("Two Base Digits："+two_base)
        print("Eight Base Digits："+eight_base)
        return True
    else:
        return False

num=11
while True:
    if(is_All_Palindrome_digits(num)):
        break
    else:
        num+=2