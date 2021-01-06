class Dictionary:

    def __init__(self):
        self.dict = {}

    def add(self, name, value):
        if name not in self.dict:
            self.dict[name] = value
            return "The item {} has just been added".format(name)
        else:
            print("{} is already present.".format(name))

    def get(self, name):
        if name not in self.dict:
            return "The item {} key has not been found".format(name)
        elif name in self.dict:
            return self.dict[name]

    def delete(self, name):
        if name not in self.dict:
            return "The item {} has not been found.".format(name)
        elif name in self.dict:
            value = self.dict.pop(name)
            return "The item {} and its value {} have been deleted.".format(name, value)

    def __repr__(self):
        return f"{self.dict}"

