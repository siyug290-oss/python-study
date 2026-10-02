# list_1 = [1,2,3,4,5,6]

# list_1.append(7)
# list_1.extend([7,8,9])
# list_1.insert(1,"哈哈")

# list_1.remove(1)
# last = list_1.pop()
# print(last)
# list_1.clear()

# list_1[2] = "干啥"
# list_1[2:] = [5,6,7,8]

# print(list_1.count(2))
# print(list_1.count(2,0,3))
# print(list_1.index(3))
# print(list_1.index(3,0,4))


# list_2 = [4,2,4,6,8,9]
# list_2.sort()
# new = sorted(list_2)
# list_2.sort(reverse=True)
# list_2.reverse()

# print([x*2 for x in range(5)])

lst = [3, 1, 2]

# 增
lst.append(4)          # 末尾加
lst.insert(0, 9)       # 在位置 0 插入

# 排序 —— 这两个的区别今天必须搞清
lst.sort()             # 当场改自己，返回 None
new = sorted(lst)      # 返回一个新列表

# 打印看看
print(lst)
print(new)

# 删
lst.remove(9)          # 按值删
last = lst.pop()       # 删最后一个，并把它返回给你
print(last)

# 查
print(3 in lst)
print(lst.index(3))
print(lst.count(3))

# 列表推导式
print([x * 2 for x in range(5)])