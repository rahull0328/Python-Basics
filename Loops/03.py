temperature = float(input("Enter the temperature in °C: "))

if temperature < 0:
    print("The temperature is below freezing.")
elif 0 <= temperature <= 100:
    print("The temperature is normal.")
else:
    print("The temperature is above boiling.")
