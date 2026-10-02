from datetime import date

y = int(input("出生年："))
m = int(input("出生月："))
d = int(input("出生日："))
birth = date(y,m,d)
today = date.today()
print((today - birth).days)