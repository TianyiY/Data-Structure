def mode1(L):
    counts=dict()
    maxkey=None
    maxvalue=-1
    for val in L:
        if val not in counts:
            counts[val]=1
        else:
            counts[val]+=1
        if counts[val]>maxvalue:
            maxkey=val
            maxvalue=counts[val]
    return maxkey

from collections import defaultdict
def mode2(L):
    counts=defaultdict(int)
    maxCount=0
    mode=0
    for eID in L:
        counts[eID]+=1
        tmp=counts[eID]
        if tmp>maxCount:
            mode=eID
            maxCount=tmp
    return mode

def mode3(L):
    counts=defaultdict(int)
    for v in L:
        counts[v]+=1
    return max(counts, key=lambda x: counts[x])

def mode4(L):
    return max(set(L), key=lambda x: L.count(x))

L=[2, 3, 4, 6, 6, 6, 7, 8]
print mode1(L)
print mode2(L)
print mode3(L)
print mode4(L)