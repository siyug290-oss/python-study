h = float(input("身高:(m)"))
w = float(input("体重:(kg)"))
bmi = w / h ** 2
if bmi < 18.5 :
    print("偏瘦")
elif bmi < 24 :
    print("正常")
elif bmi < 28 :
    print("偏胖")
elif bmi >= 28 :
    print("肥胖")




socre = int(input("你的成绩是："))
if socre > 90:
    print("A")
elif socre > 80:
    print("B")
elif socre > 70:
    print("C")
elif socre >= 60:
    print("D")
elif socre < 60 :
    print("E")

    