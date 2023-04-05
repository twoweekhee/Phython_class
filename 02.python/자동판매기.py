input_money = int(input("투입한 돈은? "))
price_goods = int(input("물건값은? "))
left_money = input_money-price_goods
coin_500 = left_money//500
coin_100 = (left_money-coin_500*500)/100

print(
    """투입한 돈 : %s\n
    물건값: %s \n
    거스름돈: %s \n
    500원 동전의 개수: %s \n
    100원 동전의 개수: %d"""
    %(input_money, price_goods, left_money, coin_500, coin_100)
)