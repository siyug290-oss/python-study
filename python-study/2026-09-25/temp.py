c1 = float(input("请输入摄氏温度："))
f1 =c1 * 9 / 5 + 32
print(f"华氏温度为：{f1:.1f}")
f2 = float(input("请输入华氏温度："))
c2 = (f2 - 32) * 5 / 9
print(f"摄氏温度为：{c2:.1f}")