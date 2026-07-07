





# f =float(input("enter temperature:"))
# celcius =(f-32) *  5/9
# print("Fahrenheit :", {f})
# c = float(input("enter temperature:"))
# Fahrenheit = (c *9/5) + 532
# print("Celcius:", {c})
# if celcious=="c":
#     print("Result", Fahrenheit)
# elif Fahrenheit=="f":
#   print("Fahrenheit:", f)


choice = input("Enter C to convert Celsius to Fahrenheit or F to convert Fahrenheit to Celsius: ").lower()

if choice == "c":
    celsius = float(input("Enter temperature in Celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    print("Result:", fahrenheit, "°F")

elif choice == "f":
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    celsius = (fahrenheit - 32) * 5/9
    print("Result:", celsius, "°C")

else:
    print("Invalid choice!")









