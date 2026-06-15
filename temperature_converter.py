def temperature_converter():
    print("Temperature Converter\n")
    print("Select input unit:")
    print("1. Celsius")
    print("2. Fahrenheit")
    print("3. Kelvin\n")

    choice = int(input("Enter choice (1/2/3): "))
    temp = float(input("Enter temperature value: "))

    if choice == 1:
        f = (temp * 9/5) + 32
        k = temp + 273.15
        print(f"\n{temp}°C = {round(f, 2)}°F = {round(k, 2)}K")
    elif choice == 2:
        c = (temp - 32) * 5/9
        k = c + 273.15
        print(f"\n{temp}°F = {round(c, 2)}°C = {round(k, 2)}K")
    elif choice == 3:
        if temp < 0:
            print("Kelvin cannot be negative.")
            return
        c = temp - 273.15
        f = (c * 9/5) + 32
        print(f"\n{temp}K = {round(c, 2)}°C = {round(f, 2)}°F")
    else:
        print("Invalid choice.")

temperature_converter()
