#외부 라이브러리
"""
#자주 쓰이는 대표 라이브러리
random    - 랜던 숫자/선택 등
time      - 시간 지연, 타이머 등
datetime  - 날짜, 시간 다루기
math      - 수학 연산 공식들
os        - 폴더, 파일 경로 관리   
"""

import random #라이브러리 적용하면 import로 먼저 주입한 후 시작해야함
"""랜덤 라이브러리를 쓰더라도 안에 조건을 몇개 짜줘야 실행 시킬 수 있음"""
e = random.choice(['Alice', 'Bob', 'Charlie']) #딕셔너러 써서 그 중에서 뽑을 수 있게 해주기
userIP = random.randint(1, 100) 

"""
#딕셔너리 변수 생성 후 random 라이브러리로 감싸는 것도 가능
#코파일럿 문제 풀이
names=["user, "admin", "guest", "hyujin", "tester""]
name = random.choice(names)
num = random.radiant(1,99)
user_id = name +str(num)   # ex: "admin23"
ip = f"{random.randint(10, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(1, 255)}"
or
prefixes = ["192.168.0.", "10.0.0.", "122.0.0."]
ip = random.choice(prefixes) + str(random.randint(1, 255))
for i in range(5):  # 5개의 랜덤 사용자 뽑기 ---->range가 숫자 연속 뽑기가 아님!!!!!!!
    # 위에서 만든 user_id, ip 생성 코드를 넣으면 됨
    print(f"생성된 사용자: {user_id} (IP: {ip})")
from datetime import datetime
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
"""

name1 = random.choice(["user1", "admin", "guest99"])
num = random.randint(1,99)
user_id = name1 +str(num) 
userIPP =f"{random.randint(10, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(1, 255)}"
for i in range(5):
    print(f"생성된 사용자: {user_id} (IP: {userIPP})")
