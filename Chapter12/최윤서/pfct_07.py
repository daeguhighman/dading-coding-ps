# 럭키 스트레이트 문제

# 수 입력 & 분리
str_N = input()
left = str_N[0 : len(str_N) // 2]
right = str_N[len(str_N) // 2 : ]

# 조건
if sum(map(int, left)) == sum(map(int, right)) :
    print("LUCKY STRAIGHT")
else :
    print("READY")