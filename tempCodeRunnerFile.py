
try:
    num1 = 1
    num2 = 3
    result = num1 / num2 # num1 = 3, num2 = 0 이라고 가정 모든 수는 0으로 나눌 수 없기 때문에 에러가 발생할 문장
    print(f'연산 결과는 {result}입니다')
except:
    print('맞지 않는 식입니다')
else:
    print('정상 동작했습니다')
finally:
    print('끝')