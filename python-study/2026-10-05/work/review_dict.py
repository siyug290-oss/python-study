items = [
    {"content":"买菜","done":False},
    {"content":"写作业","done":True},
]
for i,t in  enumerate(items,1):
    mark = "[x]" if t["done"] else "[ ]"
    print(f"{i}.{mark}{t['content']}")