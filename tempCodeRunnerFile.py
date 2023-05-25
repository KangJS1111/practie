max = 25 # 최대 허용 무게
weight = 0 # 현재 무게
item = 3 # 각 짐의 무게

while weight + item <= max: # weight와 item을 더한 값이 max 값 보다 작거나 같을 때 까지
    weight += item #weight(현재 무게)에 3을 더한다
    print(f'짐이 추가됐습니다')
print(f'총 무게는 {weight}입니다')