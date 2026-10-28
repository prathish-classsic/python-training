jewels = input("Enter jewels: ")
stones = input("Enter stones: ")

c = 0

for i in stones:
    if i in jewels:
        c += 1
print(c)
