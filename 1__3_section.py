""" for 문 기본구조
for 변수 in 반복할_자료형:
    실행항_코드""""


for i in range(5):
    print("반복 중:", i)
#    for 반복문을 활용해 1부터 10까지 숫자를 출력하는 코드를 작성한다
for i in range(11):
    print (i)    



fruits = ["사과", "바나나", "포도"]
for fruit in fruits:
    print(fruit)
#    리스트를 활용해 사용자가 좋아하는 음식 3개를 입력받고, 각각 출력하는 코드를 작성한다.
user_favorite_food = ["피카츄", "사과", "초콜릿"] 
for food in user_favorite_food:
    print(food)   


count = 0
while count < 5:
    print("카운트:", count)
    count += 1    
#while 반복문을 활용해 사용자가 "끝"을 입력할 때까지 계속 문장을 입력받는 코드를 만든다.
# 못 풀었다    
"""
while True:
    user_input = input("문장을 입력하시오 ('끝'을 입력하면 종료): ")
    if user_input == "끝":
        break
    print("입력한 문장:", user_input)
"""
#사용자가 총 3번의 기회를 갖는다. 정답 비밀번호는 "python123"으로 고정되어 있다. 사용자가 비밀번호를 입력하고, 맞으면 "접속 성공!"이라고 출력하고 프로그램 종료.
#틀리면 "비밀번호가 틀렸습니다."라고 출력한다. 3번 모두 틀리면 "접속이 거부되었습니다."라고 메세지를 출력한다.abs
"""
password = python123
count = int(password)
while count < 4:
    password = input("비밀번호를 입력하시오 (기회 3번):")
    if password =="python123":
        print("접속 성공!")
    else: 
        print("비밀번호가 틀렸습니다.")
"""
#정답

"""
count=0
while count<3:
    password= input("비밀번호를 입력하시오 (기회 3번):")
    if password=="python123":
        print("접속 성공!")
        break
    else:
        print("비밀번호가 틀렸습니다.")
        count+= 1
if count==3:
    print("접속이 거부 되었습니다.")

#if문에서 ==는 값이 같은지를 비교하는 연산자, =는 값을 할당하는 연산자      
"""
"""
import sys
count = 0  
while count < 3:    
    password = input("비밀번호를 입력하시오 (기회 3번): ")
    if password == "python123":
        print("접속 성공!")
        break
    else:
        print("비밀번호가 틀렸습니다.")
        count += 1  
if count == 3:
    print("접속이 거부되었습니다.")

#while문 전에 import sys 넣고 while 루프 안에 sys exit() 넣거나, 아님 걍 루프 안에 break 넣으면 while문이 종료된다.    
"""
#list
fav_food=["떡꼬치", "젤리", "사과"]
print(fav_food[1])
#tuple
today_ootd_color=("black", "white", "purple", "gray")
print(today_ootd_color[2])
#dictionary
user_info={"name":"eugene", "age":"23", "fav_language":"spanish"}
print(user_info['fav_language'])
#set
unique_numbers={1,2,2,2,2,3,3,2,2,4,4,5,6,7,7,7,5,5,7,4}
print(unique_numbers)

#homework 8
"""
한 명 이상의 사용자를 저장하는 딕셔너리를 만들고

각 사람의 이름과 나이를 출력하는 코드를 작성해 보세요.

for문을 활용해서 자동으로 출력되게 해보자!
"""
people1 = {"name1": "yuri", "age1": "17"}
people2 = {"name2":"james", "age2": "22"}
people3 = {"name3": "brik", "age3": "21"}
people_info= [people1, people2, people3]
for name in people_info:
    print(f"{people_info}")

#코파일럿 지적 부분
people1 = {"name": "yuri", "age": "17"}
people2 = {"name": "james", "age": "22"}
people3 = {"name": "brik", "age": "21"}
people_info = [people1, people2, people3]
for person in people_info:
    print(f"{person['name']}의 나이는 {person['age']}살입니다.")  

"""
혹시 input()으로 사람들 정보를 직접 받아서 딕셔너리 리스트를 만드는 것도 해볼래?
"""
typing_info = input("이름을 입력하시오:")
typing_info1 = input("나이를 입력하시오:")
info = {"name" :[typing_info], "age": [typing_info1]}
for list in info :
    print(f"{info['name']}의 나이는 {info['age']}살입니다.")

#수정한 코드 (리스트 없이 간단하게)
typing_info = input("이름을 입력하시오: ")
typing_info1 = input("나이를 입력하시오: ")
info = {"name": typing_info, "age": typing_info1}
print(f"{info['name']}의 나이는 {info['age']}살입니다.")

#리스트를 유지한 코드
typing_info = input("이름을 입력하시오: ")
typing_info1 = input("나이를 입력하시오: ")
info = {"name": [typing_info], "age": [typing_info1]}
print(f"{info['name'][0]}의 나이는 {info['age'][0]}살입니다.")
