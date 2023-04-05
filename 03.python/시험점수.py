score = int(input("성적을 입력하세요: "))
print("성적 : %.1f" %score)
if score >= 90 :
    print("a학점 입니다.")
elif 80<= score < 90 :
    print("b학점 입니다.")
elif 70<= score < 80 :
    print("c학점 입니다.")
elif 60<= score < 70 :
    print("d학점 입니다.")
else :
    print("f학점 입니다.")



