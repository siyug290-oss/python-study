class BankAccount :
    def __init__(self,owner,balance):
        self.owner = owner
        self.balance = balance
    
    def deposit(self,amount):
        self.balance = self.balance + amount
        self.show_balance()

    def withdraw(self,amount):
        if amount > self.balance:              
           print("当前余额不足")
        else:
            self.balance = self.balance - amount 
            self.show_balance()

    def show_balance(self):
        print(f"当前余额剩余：{self.balance:.2f}")

s1 = BankAccount("张三", 1000)
while True:
    print("-----菜单-----")
    print("------------------")
    print("1 存款 / 2 取款 / 3 退出")

    choice = input("请选择：")

    if choice == "1":
        amount = float(input("你想存入多少钱（元）？"))
        s1.deposit(amount)

    elif choice == "2":
        amount = float(input("你想取出多少钱（元）？"))
        s1.withdraw(amount)

    elif choice == "3":
        print("再见")
        break
    else:
         print("请输入1,2,3")
        



    

