import json
class TodoList:
    def __init__(self,filename="todo.json"):
        self.filename = filename
        self.items = []
        self.load()

    def add(self,content):
        if content.strip() == "":
            print("不能输入空白内容")
        else:
            self.items.append(content)
            self.save()

    def remove(self,index):
        if len(self.items) == 0:
            print("还没有待办")
        else:
            if 1 <= index <= len(self.items):
                self.items.pop(index-1)
                self.save()
            else:
                print("请输入有效数字")

    def show (self):
        if len(self.items) == 0:
            print("暂无待办")

        else:
            for i, t in enumerate(self.items,1):
                print(f"{i}.{t}")

    def load(self,):
        try:
            with open(self.filename,"r",encoding="utf-8")as f:
                self.items = json.load(f)
        except FileNotFoundError:
            self.items =[]

    def save(self):
        with open (self.filename,"w",encoding="utf-8")as f:
            json.dump(self.items,f,ensure_ascii=False,indent=2)


    

    
        


    
    


                




    

        

    def count(self):
        return len(self.items)
    