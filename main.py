answer1 = input("Type your first number   ")
num1 = float(answer1)
answer2 = input("Type your second number  ")
num2 = float(answer2)
operation = input("1 -Divide, 2 -Multiply, 3 -Add, 4 -Subtract  ")
if operation == '1':
    print(num1/num2)
if operation == '2':
        print(num1 * num2)
if operation == '3':
    print(num1+num2)
if operation == '4':
    print(num1-num2)