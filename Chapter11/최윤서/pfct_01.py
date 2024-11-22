num = input()
fear_list = list(map(int, input().split()))
fear_list.sort()

g_count, group_size= 0, 0
for fear in fear_list :
  group_size += 1
  if fear <= group_size:
    g_count += 1
    group_size = 0

print(g_count)
