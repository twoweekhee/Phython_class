num1 = int(input("첫 번째 숫자를 입력하세요: "))
symbol = input("연산기호를 입력하세요(+,-,*,/): ")
num2 = int(input("두 번째 숫자를 입력하세요: "))

if symbol == "+":
    value = num1 + num2
    print("%d + %d = %d" %(num1, num2, value))
elif symbol == "-":
    value = num1 - num2
    print("%d - %d = %d" %(num1, num2, value))
elif symbol == "*":
    value = num1 * num2
    print("%d * %d = %d" %(num1, num2, value))
elif symbol == "/":
    value = num1 / num2
    print("%d / %d = %d" %(num1, num2, value))

