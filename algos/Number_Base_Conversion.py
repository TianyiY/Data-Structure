add1, add2, conversion_base=input().split()   # conversion = number base conversion (eg. 2, 8, 10)
add1=int(add1)
add2=int(add2)
conversion_base=int(conversion_base)
Sum=add1+add2
num=0
ans=[]
if Sum==0:
    print(0)
while(Sum!=0):
    remainder=Sum%conversion_base
    ans.append(remainder)
    num+=1
    Sum//=conversion_base
for i in range(num-1, -1, -1):   # output remainder in ans in reversed order
    print(ans[i], end='')
