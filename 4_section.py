#함수(fuction) 반복되는 코드를 묶어서 이름 붙인, 비유하면 대명사

def say_hello():
    print("hi!")


say_hello()

"""
def 함수이름(매개변수):
    수행할 코드
    return 반환값
"""
#매개변수(함수에 전달한 값), return(함수가 결과로 돌려주는 값)은 선택적으로 채우기

def greet(name):
    print(f"안녕하세요, {name}님!")
greet("유진")

def plus(a, b):
    return a + b
result = plus(3, 4)
print(result) 

#과제

def introduce(name1):
    print(f"안녕하세요, 저는 {name1}입니다.")
introduce("a")    

def square(n):
    return n**n
answer = square(6)
print(answer)    

def even_or_odd1(v):
    if v % 2 ==0:
        print(f"{v}는 짝수입니다.")
    else:
        print(f"{v}는 홀수입니다.") 
even_or_odd1(7)    
#def문에 return 들어갔을때만 출력할때 변수 지정해주고 답 꺼내야 함
def even_or_odd(v):
    if v % 2 ==0:
        return(f"{v}는 짝수입니다.")
    else:
        return(f"{v}는 홀수입니다.") 
ho = even_or_odd(8)
print(ho)
'''
age=input("나이를 입력하시오:")
x=int(age)   # age=int(input("나이를 입력하시오:)) 이렇게 쓰면 더 깔끔함.
def adult(x):
    if x >= 20:
        print("성인입니다.")
    else:
        print("미성년자입니다.")
adult(x)              # 리턴 안쓰면 굳이 안에 채울 필요 없는듯  
'''
#코파일럿쌤이 다듬은 버전
def adult():
    name= input("이름을 입력하시오:")
    age1=int(input("나이를 입력하시오:"))
    if age1 >= 20:
        print(f"{name}님은 성인입니다.")
    else:
        print(f"{name}님은 미성년자입니다.")
adult()            