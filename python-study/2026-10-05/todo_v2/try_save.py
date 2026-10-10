from models import TodoList


t = TodoList()
t.add("买菜")
t.add("写作业")
t.save()
print("存盘成功")

t2 = TodoList()
t2.load()
print("读回来有",t2.count(),"条")
