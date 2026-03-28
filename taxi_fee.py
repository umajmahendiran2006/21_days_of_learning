distance = int(input("Enter distance (km): "))

if distance <= 5:
    fare = distance * 10

elif distance <= 10:
    fare = (5 * 10) + (distance - 5) * 8

else:
    fare = (5 * 10) + (5 * 8) + (distance - 10) * 5

print("Total Fare =", fare)