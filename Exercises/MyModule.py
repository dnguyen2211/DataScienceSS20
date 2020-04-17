class ListKeeper:
    def __init__(self):
        self.namedList = {"exmaple": [1,2,3,4,5]}

    def show(self):
        return self.namedList.keys()

    def add(self, name, list):
        self.namedList[name] = list

    def delete(self, name):
        return self.namedList.pop(name)

    def sort(name):
        return self.namedList[name].sort()

    def append(self, name, list):
        self.namedList[name].append(list)