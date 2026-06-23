queue = []

#enqueue
queue.append('A')
queue.append('B')
queue.append('C')
print(queue)

#dequeue
element = queue.pop(0)
print (element)


#peek
frontElement = queue[0]
print("peek:",frontElement)

#isEmpty
isEmpty = not bool(queue)
print("isEmpty:",isEmpty)

#size
print("size:",len(queue))
