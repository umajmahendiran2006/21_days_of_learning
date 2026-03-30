dist=float(input("enter distance: "))
mileage=float(input("enter mileage: "))
price=float(input("enter the fuel price per litre :"))
fule_needed=dist/mileage
total_cost=fule_needed+price
print("total cost",total_cost)