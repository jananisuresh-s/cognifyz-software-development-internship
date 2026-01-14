def temperature_converter():
    print("Temperature Converter")
    
    try:
        temp_input = input("Enter the temperature value: ")
        temp = float(temp_input)
        
        print("\nChoose conversion direction:")
        print("1. Celsius to Fahrenheit")
        print("2. Fahrenheit to Celsius")
        choice = input("Enter choice (1 or 2): ")

        if choice == '1':
            converted = (temp * 9/5) + 32
            print(f"\n{temp}°C is equal to {converted:.2f}°F")
        elif choice == '2':
            converted = (temp - 32) * 5/9
            print(f"\n{temp}°F is equal to {converted:.2f}°C")
        else:
            print("Invalid choice! Please select 1 or 2.")

        print("\nConversion complete.")

    except ValueError:
        print("Invalid input! Please enter a numeric value for temperature.")

if __name__ == "__main__":
    temperature_converter()