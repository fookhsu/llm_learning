# 前导知识， python中
# Python program to illustrate functions
# can be treated as objects
def shout(text):
    return text.upper()


def test01():
    print(shout("Hello"))
    yell = shout
    print(yell("Hello"))


def shout(text):
    return text.upper()


def whisper(text):
    return text.lower()


# can be passed as arguments to other functions
def greet(func):
    # storing the function in a variable
    greeting = func("""Hi, I am created by a function passed as an argument.""")
    print(greeting)


def test02():
    greet(shout)
    greet(whisper)


# Python program to illustrate functions
def create_adder(x):
    def adder(y):
        return x + y

    return adder


def test03():
    add_15 = create_adder(15)
    print(add_15(10))


if __name__ == "__main__":
    test03()
    pass
