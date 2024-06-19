# *args receives arguments as a tuple.
# **kwargs receives arguments as a dictionary.
def testArg1(*argv):
    for arg in argv:
        print(arg)


def testArg2(arg, *argv):
    print("First argument :", arg)
    for arg in argv:
        print("Next argument through *argv :", arg)


def testKwargs(arg, **kwargs):
    print("First arg", arg)
    for key, word in kwargs.items():
        print(key, "----", word)


# kwargs key 必须和变量名相同才可以传入
def testKwargs2(arg, a, b, c):
    print(arg)
    print(a, b, c)


# defining car class
class Car:
    # args receives unlimited number of arguments as an array
    def __init__(self, *args):
        # access args index like array does
        self.speed = args[0]
        self.color = args[1]


def testKwargs3():
    audi = Car(200, "red")
    bmw = Car(250, "black")
    print(audi.color)
    print(bmw.speed)


class Dog:
    def __init__(self, **kwargs) -> None:
        self.name = kwargs["name"]
        self.color = kwargs["color"]


def testKwargs4():
    d = Dog(name="Doggy", color="white")
    print(d.name)


def start():
    # testArg1("Hello", "Welcome", "to", "GeeksforGeeks")
    # testArg2("Hello", "Happy", "to", "learn", "Python")
    # testKwargs("Hello", a="Python", b="C++")
    kwargs = {"a": "apple", "b": "banana", "c": "cherry"}
    # testKwargs2("Hi", **kwargs)
    testKwargs3()
    pass


if __name__ == "__main__":
    start()
else:
    print("File is imported as ", __name__)
