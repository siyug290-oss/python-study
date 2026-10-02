import random
while True:
    s = input("请选择您的难度：（简单，普通，困难）")
    if s == "简单":
        answer = random.randint(1,50)
    elif s == "普通":
        answer = random.randint(1,100)
    elif s== "困难":
        answer = random.randint(1,1000)


    count = 0
    while True:
        guess = int(input("猜一个数字："))
        count = count + 1

        if guess == answer:
            print(f"猜对了，你一共用了 {count} 次")
            break
        elif guess > answer:
            print("大了")
        else:
            print("小了")
    again = input("再来一局？(y/n)")   # 在内层之外、外层之内
    if again == "n":
        break        