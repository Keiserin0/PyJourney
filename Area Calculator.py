#area calculator

menu = """
==============================
Calculate Area
please choose one of the following
A or a - Area of a Rectangle
B or b - Area of a Right-angled Triangle
C or c - Area of a Circle
Q or q - Quit
==============================
"""
#initiate inputs
length = width = base = height = radius = 0

print(menu)

choice = str(input("Please choose A, B, C or Q: ")).lower()

if choice == "a":
    length = float(input("Please enter the length: "))
    width = float(input("Please enter the width: "))
    area = length * width
    print(f"The area of the rectangle is {area:.1f}")

elif choice == "b":
    base = float(input("Please enter the base: "))
    height = float(input("Please enter the height: "))
    area = 0.5 * base * height
    print(f"The area of the right-angled triangle is {area:.1f}")

elif choice == "c":
    radius = float(input("Please enter the radius: "))
    area = 3.142 * (radius ** 2)
    print(f"The area of the circle is {area:.1f}")

elif choice == "q":
    print("Thank you for using the system\nGoodbye")

else:
    print("Invalid choice. Please select A, B, C or Q")