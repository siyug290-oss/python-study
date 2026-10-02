todos = []
while True:
    print("-----待办清单-----")
    if len(todos) == 0:
        print("(暂无待办)")
    else:
        for i, t in enumerate(todos,1):
            print(f"{i}. {t}")
    print("------------------")
    print("1 添加 / 2 删除 / 3 退出")
    choice = input("请选择：")

    if choice == "1":
        new = input("你想添加什么")
        todos.append(new)
        print("添加成功")

    elif choice == "2":
        if len(todos) == 0:
            print("还没有待办")
        else:
            num = int(input("要删除第几条？"))
            if 1<= num <= len(todos):
                todos.pop(num-1)
                print("已删除")
            else:
                print("该序号不存在,请重新输入")

    elif choice == "3":
        print("再见")
        break

    else:
        print("请输入1,2,3")
    
