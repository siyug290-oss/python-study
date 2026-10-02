i = 1
while i <= 5:
    print(i)
    i = i + 1

i = 1
while True:
    print(i)
    i = i + 1
    if i > 5:
        break

for i in range(1,11):
    if i % 2 == 0:
        continue
    print(i)