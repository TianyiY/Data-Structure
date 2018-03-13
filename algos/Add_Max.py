info={}   # dict--> key is index; value is score
num=int(input())    # input the total number of key-value pairs
while(num):
    index, val=input().split()   # input the key-value pairs and separate by space
    val=int(val)
    if index in info:   # if index is existed in dict
        info[index]=info[index]+val      # sum all the values in the same key
    else:   # if index is not in dict
        info[index]=val     # init the value to the key
    num-=1  # subtract 1 from total number

max_val=-1   # for recording the max value and its index
max_index=''

for key in info:
    if info[key]>max_val:
        max_index=key
        max_val=info[key]

print('%s %d'%(max_index, max_val))