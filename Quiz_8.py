import random

def lotto_numbers():
    numbers = random.sample(range(1, 46), 6) #중복 없는 함수
    result = f"생성된 로또 번호는 {numbers} 입니다."
    return numbers, result

# 로또 번호 생성 및 출력
numbers, output_string = lotto_numbers()
print(output_string)

