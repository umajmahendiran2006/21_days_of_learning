seconds=int(input("enter the seconds:"));
hour=seconds//3600
remaining=seconds%3600
mins=remaining//60
second=remaining%60
print(hour,":",mins,":",second)