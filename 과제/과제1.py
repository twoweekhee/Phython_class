import random 

win = 0
lose = 0


while (win < 3) and (lose < 3):
    print("=========================================================")
    user = int(input("가위바위보를 선택하세요 (1. 가위, 2. 바위, 3. 보) : "))
    rps = { 1: "가위", 2: "바위", 3: "보"}
    com = random.randint(1,3)
    print("=========================================================")
    print("당신의 선택은 ({})입니다." .format(rps[user]))
    print("컴퓨터의 선택은 ({})입니다." .format(rps[com]))
    if user == com :
        print("비겼습니다! 현재 스코어 %d승 %d패" %(win, lose))
    elif user == 1:
        if com == 2:
                lose +=1
                print("졌습니다! 현재 스코어 %d승 %d패" %(win, lose))
        elif com == 3:
                win +=1
                print("이겼습니다! 현재 스코어 %d승 %d패" %(win, lose))
    elif user == 2:
        if com == 3:
                lose +=1
                print("졌습니다! 현재 스코어 %d승 %d패" %(win, lose))
        elif com == 1:
                win +=1
                print("이겼습니다! 현재 스코어 %d승 %d패" %(win, lose))
    elif user == 3:
        if com == 1:
                lose +=1
                print("졌습니다! 현재 스코어 %d승 %d패" %(win, lose))
        elif com == 2:
                win +=1
                print("이겼습니다! 현재 스코어 %d승 %d패" %(win, lose))
    if win == 3:
        print("=========================================================")
        print("먼저 3승을 했네요. 최종승리!")
    elif lose == 3:
        print("=========================================================")
        print("먼저 3패을 했네요. 분발하세요!")
            
