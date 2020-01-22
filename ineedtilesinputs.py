# This program will ask to inout the length and width and print the needed
# when tiling a wall or floor (in m2)

length = float(input("Enter room length: "))
width = float(input("Enter room width: "))

area = length * width
needed = area * 1.05

print("You need", needed, "titles in metres squared.")
