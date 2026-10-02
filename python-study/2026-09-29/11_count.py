words = ["apple", "banana", "apple", "cherry", "banana", "apple"]

counts = {}
for w in words:
    counts[w] = counts.get(w,0) + 1

print(counts)


def take_second(x):
    return x[1]
print(sorted(counts.items(),key=take_second,reverse=True)[:5])
print(sorted(counts.items(),key=lambda x :x[1],reverse=True)[:5])




fruits = ["apple", "banana"]
for i,f in enumerate(fruits):
    print(i,f)



names = ["张三", "李四"]
scores = [95,88]
for n,s in zip (names,scores):
    print(n,s)