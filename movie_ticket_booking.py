total_amount = 0

n = int(input("Enter number of tickets: "))

for i in range(n):
    age = int(input(f"Enter age of person {i+1}: "))
    day = input("Is it weekend? (yes/no): ").lower()
    
    # Price calculation
    if age < 12:
        price = 100
    else:
        price = 200

    if day == "yes":
        price += 50

    total_amount += price

print(f"\nTotal Ticket Price: ₹{total_amount}")