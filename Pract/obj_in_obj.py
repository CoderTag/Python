class Jungle(object):
    def __init__(self):
        self.amazon = "Amazon"

    def show_jungle(self):
        print(self.amazon)


class MangoOrchid(object):
    def __init__(self):
        self.myOrchid = "Dasheri"
        self.fromForest = Jungle()

    def show_orchid(self):
        self.fromForest.show_jungle()
        print(self.myOrchid)


obj = MangoOrchid()
obj.show_orchid()
