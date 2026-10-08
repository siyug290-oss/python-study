from models import TodoList

t = TodoList()

while True:
    t.show()
    print("1.添加  2.删除  3.退出")
    choice = input("请输入数字")

    if choice == "1":
        t.add(input("要添加点什么"))

    elif choice == "2":
        t.remove(int(input("要删除哪一条")))

    elif choice == "3":
        print("再见")
        break

    else:
        print("请输入1，2，3")


