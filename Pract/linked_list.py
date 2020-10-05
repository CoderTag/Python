class Node(object):
    """Node of a linked list"""

    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    def insert_node(self, data):

        if self.next_node is None:
            self.next_node = Node(data)

        else:
            nextptr = self.next_node
            while True:
                if nextptr.next_node is None:
                    nextptr.next_node = Node(data)
                    break
                else:
                    nextptr = nextptr.next_node

    def list_node(self):
        nextptr = self.next_node
        print(self.data)
        while True:
            if(nextptr == None):
                break
            else:
                print(nextptr.data)
                nextptr = nextptr.next_node


root_node = Node(10)
root_node.insert_node(20)
root_node.list_node()
root_node.insert_node(30)
root_node.insert_node(40)
root_node.insert_node(50)
root_node.insert_node(60)
root_node.list_node()
