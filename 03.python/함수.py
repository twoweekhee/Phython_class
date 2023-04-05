import math

x = int(input("첫번째 점의 x값을 입력하세요 : "))
y = int(input("첫번째 점의 y값을 입력하세요 : "))
x2 = int(input("두번째 점의 x값을 입력하세요 : "))
y2 = int(input("두번째 점의 x값을 입력하세요 : "))

print((x,y), (x2,y2))

d_before= (x-x2)**2+(y-y2)**2
d = math.sqrt(d_before)

print("두 점의 거리는 : %f" %d)
