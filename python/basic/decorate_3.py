def hello_decorator(func):
    def inner1(*args):

        print("before Execution")

        # getting the returned value
        print(args)
        returned_value = func(*args)
        print("after Execution")

        # returning the value to the original frame
        return returned_value

    return inner1


# adding decorator to the function
@hello_decorator
def sum_two_numbers(a, b):
    print("Inside the function")
    return a + b


a, b = 1, 2

# getting the value through return of the function
print("Sum =", sum_two_numbers(a, b))


# code for testing decorator chaining
def decor1(func):
    def inner(*args):
        print("decor 1 befor func")
        x = func(*args)
        print("decor 1 after func")
        return x * args[0]

    return inner


def decor2(func):
    def inner(*args):
        print("decor 2 befor func")
        x = func(*args)
        print("decor 2 after func")
        print(args)
        return 2 + x

    return inner


@decor1
@decor2
def num(a):
    return a


@decor2
@decor1
def num2(a):
    return a


"""
装饰顺序
@d1
@d2
def foo()
...
---------------> d1(d2(foo()))
"""
print(num(5))
print(num2(5))
