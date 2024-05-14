
# __del__ ----------This is to destroy an object , del function automatically executes

class destroy:
    def __del__(self):
            print("Destroy the object")
d=destroy()

del d


