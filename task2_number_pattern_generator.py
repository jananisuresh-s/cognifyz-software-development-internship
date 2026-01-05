def generate_pattern():
    print("Number Pattern Generator")
    
    try:
        rows = int(input("Enter the number of rows for the pyramid: "))
        
        print(f"\nGenerating a {rows}-level pyramid:\n")
        
        for i in range(1, rows + 1):
            for j in range(rows - i):
                print(" ", end="")
            
            for k in range(1, i + 1):
                print(k, end=" ")
            
            print()
            
        print("\nPattern generation complete.")
        
    except ValueError:
        print("Invalid input! Please enter an integer.")

if __name__ == "__main__":
    generate_pattern()