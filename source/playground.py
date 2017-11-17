from linkedlist import *

# items = ['A', 'B', 'C']
items = []
linked_list = LinkedList(items)

first = linked_list.append("A")
first_item = linked_list.items()
# print(first_item)

first = linked_list.prepend("B")
second_item = linked_list.items()
print(second_item)

# print(linked_list.length)
