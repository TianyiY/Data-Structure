n=int(input())  # input a number
counter=0
while n!=1:
    if n%2==0:  # even number
        n=n/2
    else:   # odd number
        n=(3*n+1)/2
    counter+=1
    print('step: ', counter, '  n=', n)