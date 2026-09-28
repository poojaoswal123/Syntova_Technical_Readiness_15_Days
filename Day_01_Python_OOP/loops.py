# Loops
# for , while

# for
for i in range(1, 6):
    print(i)

# loop through a list
names = ["Pooja", "A", "B"]
for n in names:
    print(n)

# while:
i = 1
while i <= 5:
    print(i)
    i += 1

# break:
for i in range(1,10):
    if i == 5:
        break
    print(i)

# continue:
for i in range(1,10) :
    if i == 5:
        continue
    print(i)

# exmaple : sum 1 to 100:
total = 0
for i in range(1,101):
    total += i
print(total)

