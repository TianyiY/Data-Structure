s=[0]*100
for i in range(1, 100):
    for j in range(i, 100):
        if ((j+1)%(i+1)==0):
            if (s[j]==0):
                s[j]=1
            else:
                s[j]=0
print(s)