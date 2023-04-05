a=200
b=100
print(a==b, a>b) #값이 boolean 값으로 나온다.

name = input("input youy name: ")
age = int(input("write your age: "))
height = int(input("write your height: "))

if (age>=10) and (height>=135) :
    print(name," can ride this attraction" )
else : print(name," can't ride this attraction" )