tup = [1,2,76,89,128]
tup[0] = 90
print(type(tup),tup)
print(len(tup))
print(tup[0])
print(tup[1])
print(tup[2])
print(tup[3])
print(tup[4])
i = int(input("Enter the number: "))
if i in tup:
    print("YES it is in tup")
else:
    print("NO")
tup2 = tup[1:4]
print(tup2)
tup.extend(tup2)
print(tup)


