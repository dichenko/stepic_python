class ExtendedStack(list):
    def sum(self):
        x = self.pop()
        y = self.pop()
        self.append(x + y)

    def sub(self):
        x = self.pop()
        y = self.pop()
        self.append(x - y)

    def mul(self):
        x = self.pop()
        y = self.pop()
        self.append(x * y)

    def div(self):
        x = self.pop()
        y = self.pop()
        self.append(x // y)

    def printStack(self):
        for i in range(len(self)-1, -1,-1):
            print(self[i])
        print('__________________')

a = ExtendedStack()

a.append(1)
a.append(3)
a.append(5)
a.append(6)
a.printStack()
a.sum()
a.printStack()
