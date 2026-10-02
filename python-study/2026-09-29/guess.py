import random
answer = random.randint(1, 100)

for i in range (10):
    num = int(input("请输入一个数字"))
    if num < answer:
        print("小了")
    elif num > answer:
        print("大了")
    else:
        print("猜对了")
        break
else:
    print("游戏结束，你没有猜中")
print(f"你一共用了{i + 1}次机会")



