col, char=input().split()
col=int(col)  # how many columns
if col%2==1: # odd number
    row=col//2+1   # return integer
else:
    row=col//2
for i in range(0, col):
    print(char, end='')   # output the first row, end='' for not changing line
print('')
#print('\n')
for i in range(2, row):
    print(char, end='')
    for j in range(col-2):
        print(' ', end='')
    print(char)
for i in range(0, col):
    print(char, end='')    # output the last row