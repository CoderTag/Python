from random import randrange


class Node(object):
    data = None
    link = None


class LinkedList(object):
    def __init__(self):
        self.head = None
        self.size = 0

    def insertAtEnd(self, data):
        node = Node()
        node.data = data
        node.link = None

        if self.head == None:
            self.head = node

        else:
            n = self.head
            while(n.link != None):
                n = n.link
            n.link = node

        self.size += 1

    def show(self, pos='all'):
        if self.size == 0:
            print("Link is empty")
            return

        if(pos == "all"):
            n = self.head
            while(n.link != None):
                print(n.data)
                n = n.link
            print(n.data)

    def count(self):
        return self.size

    def insertAtPos(self, pos, data):
        try:
            if pos < 1 or pos > (self.size + 1):
                raise Exception('Postion Out of range')
            node = Node()
            node.data = data
            if pos == 1:
                node.link = self.head
                self.head = node
                self.size += 1

            elif pos == (self.size + 1):
                self.insertAtEnd(data)

            else:
                n = self.head
                while(pos > 1):
                    priv = n
                    n = n.link
                    pos -= 1
                priv.link = node
                node.link = n
                self.size += 1

        except Exception as e:
            print("Exception: ", e)


# Testing LinkedList
a = LinkedList()
for i in range(5):
    r = randrange(100, 1000)
    a.insertAtEnd(r)
a.show()
print(f"size of list {a.count()}")
a.insertAtPos(3, 45)
print("##############\n")
a.show()
print(f"size of list {a.count()}")
