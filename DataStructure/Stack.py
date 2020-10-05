class Stack:
    def __init__(self):
        self.top = 0
        self.arr = []

    def mypush(self, data):
        self.arr.append(data)
        self.top += 1

    def mypop(self):
        self.top -= 1

    def myshow(self):
        for i in range(0, self.top):
            print(self.arr[i], end=" ")
        print()


s = Stack()
s.mypush(22)
s.mypush(44)
s.mypush(78)
s.mypush(96)
s.myshow()
s.mypop()
s.myshow()
