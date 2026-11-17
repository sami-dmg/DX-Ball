def calculate_slope():
    
    print("--- Enter coordinates for Point 1 ---")
    x1 = float(input("Enter value for x1: "))
    y1 = float(input("Enter value for y1: "))
    
    print("\n--- Enter coordinates for Point 2 ---")
    x2 = float(input("Enter value for x2: "))
    y2 = float(input("Enter value for y2: "))
    
    # Check for division by zero (vertical line case)
    if x2 - x1 == 0:
        print("\nResult: Slope is undefined. This is a vertical line.")
    else:
        m = (y2 - y1) / (x2 - x1)
        print(f"\nCalculated Slope (m) = {m}")

# Run the function
calculate_slope()