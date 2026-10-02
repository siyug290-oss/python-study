h = float(input("身高:(m)"))
w = float(input("体重:(kg)"))
bmi = w / h ** 2
low = 18.5 * h ** 2
high = 24 * h ** 2
print(f"你的bmi为:{bmi:.1f}")
print(f"你的健康区间为：{low:.1f}到{high:.1f}")