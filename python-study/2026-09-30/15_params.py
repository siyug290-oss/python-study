def greet(name,greeting="你好"):
    print(f"{greeting},{name}")


greet("Siyu")
greet("Siyu","早上好")
greet(greeting="早",name="Siyu")


def total(*numbers):
    result = 0
    for n in numbers:
        result = result + n
    return result

print(total(1,2,3))
print(total(1,2,3,4,5))




def f():
    x = 10

f()
print(x)
