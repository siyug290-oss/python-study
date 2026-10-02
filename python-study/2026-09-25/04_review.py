name = "Siyu"
age = 18
height = 1.75
is_student = True

print(name,type(name))
print(age,type(age))
print(height,type(height))
print(is_student,type(is_student))


name = "Siyu"
school = "南京大学"
major = "计算机"
height = 1.75

print(f"你的名字是{name}")
print(f"你的大学是{school}")
print(f"你的专业是{major}")
print(f"你的身高为{height:.1f}米")
print(f"你的身高为{height * 100:.0f}厘米")

name = input("你的名字：")
age = int(input("你的年龄："))

print(f"{name},一年后你{age + 1}岁")
print(f"十年后，你{age + 10}岁")