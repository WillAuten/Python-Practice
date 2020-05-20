from node import Node
from arrays import Array

array = Array(5)
for i in range(len(array)):
    array[i] = i + 1

print("Our Array is",array)

head = None
for item in array:
    head = Node(item, head)
    print(head.data)
    head = head.next
