L=[50, 88, 27, 58, 30, 21, 58, 13, 84, 24, 29, 43, 61, 44, 65, 74, 76, 30, 82, 43]

# left child of node index i
def left(i):
    return i*2+1
# right child of node index i
def right(i):
    return i*2+2
# parent of left child index i
def parent(i):
    return (i-1)/2
# root node
def root(i):
    return i==0
# leaf (without any children)
def leaf(L, i):
    return right(i)>=len(L) and left(i)>=len(L)
# node with only one child
def one_child(L, i):
    return right(i)==len(L)

# call this if the heap rooted at i satisfies the heap property
def down_heapify(L, i):
    # if i is a leaf, heap property holds
    if leaf(L, i):
        return
    # if node index i has one child
    if one_child(L, i):
        # check heap property (compare itself with its only left child)
        if L[i]>L[left(i)]:
            (L[i], L[left(i)])=(L[left(i)], L[i])
        # otherwise, return
        return
    # if node i has two children, check property (compare)
    # if node i is smaller than its children, return
    if min(L[left(i)], L[right(i)])>=L[i]:
        return
    # otherwise, swap (compare two children and decide which to swap)
    if L[left(i)]<L[right(i)]:
        (L[i], L[left(i)])=(L[left(i)], L[i])
        down_heapify(L, left(i))
        return
    else:
        (L[i], L[right(i)]) = (L[right(i)], L[i])
        down_heapify(L, right(i))
        return

# up heapify
def up_heapify(L, i):
    L[i]<L[parent(i)]
    (L[parent(i)], L[i])=(L[i], L[parent(i)])
    i=parent(i)