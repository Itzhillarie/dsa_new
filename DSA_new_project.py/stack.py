stack = []

#push
stack.append("A")
stack.append("B")
stack.append("C")
print(stack)

#pop
item = stack.pop()
print(item)
print(stack)


#peek
#top_item = stack.Peek
#print(top_item)
print(stack[0])
  

#check if stack is empty
if not stack:
    print ("stack is empty")

