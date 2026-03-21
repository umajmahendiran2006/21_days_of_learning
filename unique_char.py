string = str(input("Enter the string: "))
res = []   
for i in string:
    if i not in res:
        res.append(i)
    else:
        a = "not a unique_characters"
        break
else:
    a = "unique_characters"

print(a)