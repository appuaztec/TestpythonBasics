#Declare variables inside class


class Variableinside:
    x,y=10,30 # class variables
    def add(self):
        print(self.x+self.y)


    def mul(self):
        print(self.x*self.y)


vi=Variableinside()
vi.add()
vi.mul()