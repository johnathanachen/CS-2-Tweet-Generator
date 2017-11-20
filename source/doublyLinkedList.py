class DoublyLinkedNode(object):
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None


class DoublyLinkedList(object):

    def __init__(self):
        self.head = None
        self.tail = None
