num = int(input("숫자를 입력하세요."))
format = ("입력한 숫자는 : %s"%num)
if num%2==0 :
    print(format, ", 짝수입니다.")
else: 
    print(format, ", 홀수입니다.")
