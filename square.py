n = int(input("Enter total numbers: "))
squares = []
for i in range(n):
    num = int(input("Enter number: "))
    squares.append(num * num)
print("Squares:", squares)