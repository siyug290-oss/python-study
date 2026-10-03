try:
    int("abc")
except ValueError:
    print("ValueError")

try:
    lst = [1,2,3,4,5]
    print(lst.index(6))
except ValueError:
    print("ValueError")

try:
    d = {"a": 1, "b": 2}
    print(d["c"])              # 字典里没有 "c"
except KeyError:
    print("KeyError")
try:
    a = 8 / 0
except ZeroDivisionError:
    print("ZeroDivisionError")

while True:
    try:
        num = int(input("请输入一个数字:"))
        print(num)
        break
    except ValueError:
        print("你输入的不是一个数字,请重试")

try:
    nums = [1, 2, 3]
    print(nums[99])            # 索引 99 不存在
except IndexError:
    print("IndexError")

