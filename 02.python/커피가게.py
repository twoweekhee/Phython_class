num_ame = int(input("아메리카노는 몇잔 팔았나요?"))
num_latte = int(input("라떼는 몇잔 팔았나요?"))
num_caffuchino = int(input("카푸치노는 몇잔 팔았나요?"))

price_ame = 2000
price_latte = 3000
price_caffuchino = 3500

sum = num_ame*price_ame + num_latte*price_latte + num_caffuchino*price_caffuchino

print("아메리카노 판매수 : {}\n카페라떼 판매수 : {}\n카푸치노 판매구 : {}\n총 매출은 {}원 입니다." 
.format(num_ame, num_latte, num_caffuchino, sum))