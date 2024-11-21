s = list(map(int, input()))
answer = s[0]
for i in s[1:]:
  if answer == 0 : answer += i
  else: answer *= i

print(answer)