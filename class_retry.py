"""
https://jimmy-ai.tistory.com/239
"""

#방법 1: sorted() 사용 (가장 간단한 방식)
numbers = [2, 22, 54, 7, 9, 4, 23, 5, 78, 4, 23455346534, 43342, 43567]
sorted_numbers = sorted(numbers)  # 리스트 정렬
for num in sorted_numbers:
    print(num)

#방법 2: sort() 사용 (리스트 자체 변경)
numbers.sort()  # 리스트 자체를 정렬
for num in numbers:
    print(num)

#방법 3: 버블 정렬 (for문만 사용)
numbers = [2, 22, 54, 7, 9, 4, 23, 5, 78, 4, 23455346534, 43342, 43567]
for i in range(len(numbers) - 1):
    for j in range(len(numbers) - i - 1):
        if numbers[j] > numbers[j + 1]:  # 앞 숫자가 크면 자리 교환
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
for num in numbers:
    print(num)

    