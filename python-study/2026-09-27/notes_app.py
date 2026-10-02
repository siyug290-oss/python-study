test = input("请输入一段话：")
with open("notes.txt","a",encoding="utf-8") as f:
    f.write(test + "\n")

with open("notes.txt","r",encoding="utf-8") as f:
    print(f.read())
