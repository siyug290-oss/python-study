class TodoList:
    def __init__(self):
        self.items = []

    def add(self,content):
        if content.strip() == "":
            print("不能输入空白内容")
        else:
            self.items.append(content)

    def remove(self,index):
        if len(self.items) == 0:
            print("还没有待办")
        else:
            if 1 <= index <= len(self.items):
                self.items.pop(index-1)
            else:
                print("请输入有效数字")

    def show (self):
        if len(self.items) == 0:
            print("暂无待办")

        else:
            for i, t in enumerate(self.items,1):
                print(f"{i}.{t}")


    
    


                




    

        

    def count(self):
        return len(self.items)
    