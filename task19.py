text = input("Matin kiriting >> ")

s = 0
for i in text:
    if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
        s += 1
print(s)