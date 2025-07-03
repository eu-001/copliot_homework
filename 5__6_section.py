
# "w" = write mode , 'with open () as f:' <-- 파일을 열고 자동을 닫힘
# .write() <-- 문자열만 저장됨
with open("log.txt", "w", encoding="utf-8") as f:
    f.write("유진 접속 성공!\n")
# "a" = append mode, 기존에 쓰던 파일에 내용을 뒤에 이어 붙여서 씀
with open("log.txt", "a", encoding="utf-8") as f:
    f.write("추가 기록입니다!\n") 
# "r" = read mode, .read() <-- 파일 전체 내용을 문자열로 가져옴
with open("log.txt", "r", encoding="utf-8") as f:
    content = f.read()
    print(content)      
'''
#과제
def adult(name,age):
    if age>= 20:
        return f"{name}님은 성인입니다."
    else:
        return f"{name}님은 미성년자입니다."
x = input("이름을 입력하시오:")
y = int(input("나이를 입력하시오:"))
t = adult(x,y)             
with open("homework.txt", "w", encoding="utf-8") as f:
    f.write(f"{t}\n") #문자열 t를 가져오고 싶을때는  f"." 이렇게 써야함!
with open("homework.txt", "a", encoding="utf-8") as f:
    f.write(f"{t}\n") 
with open("homework.txt", "r", encoding="utf-8") as f:
    content1 = f.read()
    print(content1)        
'''    

# def is_adult(name,age):
#     if age >= 20:
#         return f"{name}은 성인입니다."
#     else:
#         return f"{name}은 미성년자입니다."
# w = input("이름을 입력하시오:")
# m = int(input("나이를 입력하시오:"))
# k = is_adult(w,m)
# with open("users_log.txt", "w", encoding="utf-8") as f:
#     f.write(f"{k}\n")
# with open("users_log.txt", "a", encoding="utf-8") as f:
#     f.write(f"{k}\n")
# with open("users_log.txt", "r", encoding="utf-8") as f:
#     logs= f.read(); print(logs)
'''
""" 여러 매개변수 + 리턴 값"""
def calculate_total(price, count):
    total= price * count
    return total
result = calculate_total(2000, 3)
print(f"총 가격은 {result}원 입니다.")

"""조건에 따라 다른 결과 리턴"""
def get_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    else:
        return "C 이하"
grade = get_grade(87)
print("등급", grade)    

"""함수에서 여러 값 리턴(튜플)"""
def get_user():
    name = "유진"
    age = 23
    return name, age
n, a = get_user()
print(f"{n}님의 나이는 {a}살 입니다.")   
'''
#homework
def get_basic_info():
    name = input("이름을 입력하시오:")
    age = int(input("나이를 입력하시오:"))
    fav_color = input("좋아하는 색깔을 입력하시오:")
    print(f"가장 좋아하는 색깔은 {fav_color}입니다.")  
    return name, age 
get_basic_info()      
#return이 함수의 중간에 있으면 그 뒤에 잇는 코드가 더 이상 실행되지 않음!
#return은 최후에 둬야 함!