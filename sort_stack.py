class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


def sort_stack(old_stack):
    # sort the old stack in descending order

    # create a new stack to store the sorted numbers
    new_stack=Stack()

    # ensure there are numbers in stack
    if old_stack.size()==0:
        print 'No element in stack'
        return

    else:
        # while the old stack is not empty
        while old_stack.size()!=0:
            # record the top element in the old stack, temp_min is a temp variable for comparison
            temp_min=old_stack.pop()
            # compare every element in the new stack with the temp variable to find the min element
            while new_stack.size()!=0 and new_stack.peek()>temp_min:
                # push the bigger element into the old stack
                old_stack.push(new_stack.pop())
            # push the smaller element into the new stack
            new_stack.push(temp_min)
    return new_stack


old_stack=Stack()
old_stack.push(3)
old_stack.push(5)
old_stack.push(8)
old_stack.push(4)
old_stack.push(2)
old_stack.push(6)

new_stack=sort_stack(old_stack)


for i in range(new_stack.size()):
    print new_stack.pop()
