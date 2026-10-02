S = input("请输入一串英文内容：")
print(len(S))
print(len(S.replace(" ","")))
words = S.split()
print(len(words))
print(words[0])
print(words[-1])

f = input("查询某个指定词出现的次数：")
print(S.count(f))
print(S.upper())

