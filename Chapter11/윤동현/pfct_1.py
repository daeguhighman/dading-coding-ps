N = int(input())
numbers = sorted(list(map(int, input().split())))

group = 0
members = 0
for num in numbers:
  members = members + 1
  if num <= members:
    members = 0
    group = group+1

print(group)

