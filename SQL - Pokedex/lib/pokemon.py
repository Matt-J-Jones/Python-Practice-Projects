class Pokemon:
    def __init__ (self, id, name, height, weight, types, pic):
        self.id = id
        self.name = name
        self.height = height
        self.weight = weight
        self.types = types
        self.pic = pic

    def getID(self):
        return self.id

    def getName(self):
        return self.name

    def getHeight(self):
        return self.height

    def getWeight(self):
        return self.weight

    def getTypes(self):
        types = []
        for t in self.types:
            types.append(t['type']['name'])
        return ', '.join(types)
    
    def getPic(self):
        return self.pic

    def printAll(self):
        print(f"ID: {self.id}")
        print(f"Name: {self.name}")
        print(f"Height: {self.height}")
        print(f"Weight: {self.weight}")
        print(f"Types: {self.getTypes()}")
