class Student:
    def __init__(self,name,score):
        self.name = name
        self.score = score

    def say_hello(self):
        print(f"我是{self.name},成绩{self.score}")

    def is_pass(self):
        return self.score >= 60

s1 = Student("张三",95)
s1.say_hello()
print(s1.is_pass())

s2 = Student("李四",55)
s2.say_hello()
print(s2.is_pass())

s3 = Student("王五",100)
s3.say_hello()
print(s3.is_pass())