strings = ["adaaa", "adccc", "adddd"]

for i in strings:
    print(i[-3:])


x = [x[-3:] for x in strings]
print(x)

