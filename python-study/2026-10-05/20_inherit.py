class Animal:
    def __init__(self,name):
        self.name = name

    def speak(self):
        return "......"

    def __str__(self):
        return f"一只叫{self.name}的动物"

class Dog(Animal):
    def speak(self):
        return "汪汪"

    def __str__(self):
        return f"一只叫{self.name}的狗"

    def __len__(self):
        return 4


class Cat(Animal):
    def speak(self):
        return "喵喵"

    def __str__(self):
        return f"一只叫{self.name}的猫"


animals = [Dog("旺财"), Cat("咪咪"), Dog("大黄")]
for a in animals:
    print(a, "说：", a.speak())


print()
print("len(第一条)=",len(animals[0]))