# total = 0
# i = 1
# while i <= 100:
#   total += i
#   i += 1
# print(total)


# total = 0
# i = 1
# while True:
#   total += i
#   i += 1
#   if i > 100:
#     break
# print(total)

# 偶数求和
total = 0
for i in range(1,101):
  if i % 2 != 0:
    continue
  total += i
print(total)