n = input("Enter number: ")

s = 0
p = 1

for i in n:
    digit = int(i)
    s = s + digit
    p = p * digit   

if s == p:
    print("spy number")
else:
    print("not a spy number")   