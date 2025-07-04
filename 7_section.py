#예외 처리
""" 기본 구조
try:
    #위험할 수 있는 코드
except 예외타입:
    #예외가 발생했을 때 실행할 코드"""    

"""
#예시
try:
    age = int(input("나이를 숫자로 입력하세요:"))
except ValueError:
    print("숫자로 입력해야 합니다.")

try:
    with open("missing.txt", "r") as f:
        data = f.read()
except FileNotFoundError:
    print("파일을 찾을 수 없습니다.") 
"""           

# def user_info():
#     name = input("이름을 입력하시오:")
#     try:
#         age = int(input("나이를 입력하세요:"))
#     except ValueError:
#         print("숫자로 입력해야 합니다.")              
# user_info()

#코파일럿의 업그레이드 버전
def user_info():
    name = input("이름을 입력하시오:")
    while True: #while문을 씀으로써 성공할때까지 올바른 답변을 받을 수 있음!
        try:
            age = int(input("나이를 입력하세요:"))
            break # 성공하면 반복문 종료됨
        except ValueError:
            print("숫자로 입력해야 합니다. 다시 시도하세요.")
    print(f"{name}님의 나이는 {age}살입니다.") 
#user_info()           


"""
try:
    실행해볼 코드 (여기서 에러 날 수도 있음)
except 예외타입:
    에러 발생했을 때 실행할 코드
finally:
    에러가 나든 안 나든 '무조건' 실행되는 코드

----> 로그 시스템. 보안 감지기. 자동화 툴에서는 "기록은 무조건 남겨야 해!" -> 에러가 나더라도
finally 블록에서 로그 저장! """


# #예시
# def save_log(name_input):
#     try:
#         age = int(input("나이를 입력하시오:"))
#         result = f"{name_input}, {age}살 - 입력 성공" #터미널에 출력 되는게 아니라 파일에 저장이 됨
#     except ValueError:
#         result = f"{name_input} - 나이 입력 실패 (숫자 아님)" #터미널에 출력 되는게 아니라 파일에 저장이 됨
#     finally:
#         with open("user_log.txt", "a", encoding="utf-8")as f:
#             f.write(result + "\n")    #터미널에 출력 되는게 아니라 파일에 저장이 됨    
# username = input("이름을 입력하시오:")
# #save_log(username)            

#미션
def logiin_try():
    try:
        userID = input("아이디를 입력하시오:")
        userIP = input("아이피주소를 입력하시오:") #짜피 순수 숫자로 입력하는게 아니므로 int 쓸 필요가 없음!
        if userIP.startswith("192.") or userIP.endswith(".255"):
            result1 = f"[{userID}] - 의심 접속 탐지 (IP: {userIP})" #if문의 참인 경우를 초점에 맞춰서 의심 접속 탐지를 찾기
        else:
            result1 = f"[{userID}] - 정상 접속 (IP: {userIP})"  
    except ValueError: 
        result1 = f"[{userID}] - 예외 발생 (입력 오류)" #아예 구조 자체가 이상한 경우로
    finally:
        with open("access_log.txt", "a", encoding="utf-8")as f:
            f.write(result1 + "\n")
        print("로그 저장 완료!")    
logiin_try()                