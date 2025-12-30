stack=[]

#push means add the element of the stack
stack.append(15)
stack.append(25)
stack.append(45)
print("stack",stack)

#peek return last element in the list
top_Element = stack[-1]
print("peek",top_Element)

#pop means remove the element from stack
poppedElement = stack.pop()
print("popped",poppedElement)

#stack after pop
print("stack after pop",stack)

#isEmpty list is empty are not
isEmpty =not bool (stack)
print("isEmpty",isEmpty)

#size of stack
print("size",len(stack))



