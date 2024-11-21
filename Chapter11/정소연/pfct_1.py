n = int(input())
data = list(map(int, input().split()))

numOfGroup = 0

while data:
    data.sort(reverse=True)
    max_value = data[0]
    
    if len(data) >= max_value:
        data = data[max_value:]
        numOfGroup += 1

    else: break


print(numOfGroup)