class MyStuffClass(object):
    def __init__(self):
        self.name="This is class variable"

    def apple(self):
        print("I am Apple")


things = MyStuffClass()
things.apple()
print(things.name)
