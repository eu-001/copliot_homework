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
