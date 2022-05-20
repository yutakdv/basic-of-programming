print("키와 몸무게를 미국 표준 단위로 변환해 드립니다.")
cm = int(input("손님의 키를 센티미터 단위로 입력하세요. "))
print("키는 %d 센티미터 입니다." %cm)
kg = int(input("손님의 몸무게를 킬로그램 단위로 입력하세요. "))
print("몸무게는 %d 킬로그램 입니다." %kg)
print("손님의 키와 몸무게는 다음과 같습니다.")

def cm2foot(n):
    return 0.032808399 * n 

def kg2pound(n):
    return 2.2046226218 * n

def foot_rest_inch(n):
    return (cm2foot(cm) - int(cm2foot(cm))) * 12

print(int(cm2foot(cm)), "피트", round(foot_rest_inch(cm)), "인치")
print(int(kg2pound(kg)), "파운드")
print("저희 서비스를 이용해주셔서 감사드립니다.")

