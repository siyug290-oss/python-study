import sqlite3
class TodoList:
    def __init__(self,db : str ="todo.db")->None:
        self.conn = sqlite3.connect(db)
        self.conn.execute("""
                  CREATE TABLE IF NOT EXISTS todos(
                  id INTEGER PRIMARY KEY AUTOINCREMENT,
                  content TEXT NOT NULL,
                  done INTEGER NOT NULL DEFAULT 0)
                   """ )
        self.conn.commit()
        self.items:list[dict] = []
        self.load()

    def add(self,content : str)->None:
        if content.strip() == "":
            print("不能输入空白内容")
            return
        self.conn.execute(
            "INSERT INTO todos (content, done) VALUES (?, 0)", (content,)
        )
        self.conn.commit()
        self.load()

    def remove(self,index:int)->bool:
        if len(self.items) == 0:
            print("还没有待办")
            return False
        else:
            if 1 <= index <= len(self.items):
                todo_id = self.items[index-1]["id"]
                self.conn.execute("DELETE FROM todos WHERE id = ?", (todo_id,))
                self.conn.commit()
                self.load()
                return True
            else:
                print("请输入有效数字")
                return False

    def show (self)->None:
        if len(self.items) == 0:
            print("暂无待办")

        else:
            for i, t in enumerate(self.items,1):
                mark = "[x]" if t["done"] else "[ ]"
                print(f"{i}. {mark} {t['content']}")
            
                

    def load(self)->None:
        rows = self.conn.execute("SELECT id ,content , done FROM todos ORDER BY id")
        self.items = [
            {"id": r[0], "content": r[1], "done": bool(r[2])}
            for r in rows
        ]

    def count(self)->int:
        return len(self.items)

    def done(self,index:int)->bool:
        if len(self.items) == 0:
            print("暂时还没有待办")
            return False
        else:
            if 1<= index <= len(self.items):
                todo_id = self.items[index-1]["id"]
                self.conn.execute("UPDATE todos SET done = 1 WHERE id = ?", (todo_id,))
                self.conn.commit()
                self.load()
                return True
            else:
                print("输入的数字不存在，请重输")
                return False

    def undone(self,index:int)->bool:
        if len(self.items) == 0:
            print("暂时还没有待办")
            return False
        else:
            if 1<= index <=len(self.items):
                todo_id = self.items[index-1]["id"]
                self.conn.execute("UPDATE todos SET done = 0 WHERE id = ?", (todo_id,))
                self.conn.commit()
                self.load()
                return True
            else:
                print("请输入有效数字")
                return False

        
    
