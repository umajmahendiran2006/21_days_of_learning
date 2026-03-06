weight=float(input("enter your weight: "))
height=float(input("enter your height: "))
bmi_value = weight / (height ** 2)
if bmi_value <= 18.5:
    print("Underweight")
elif 18.5 < bmi_value <= 25.0:
    print("Normal")
elif 25.0 < bmi_value <= 30.0:
    print("Overweight")
else:
    print("Obese")