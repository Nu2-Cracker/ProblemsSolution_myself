# https://atcoder.jp/contests/abc201/tasks/abc201_c


S = list(input())

def solve():
  used = 0
  unused=0
  unknown=0
  for si in S:
    if si == "o":
      used += 1
    elif si == "x":
      unused += 1
    else:
      unknown += 1

  if used > 4:
    return 0
  if (unused + used) < 1:
    return 0

  res = 0
  print(used)
  print(unused)
  print(unknown)


print(solve())



# if si == "o":
#   password += i
# elif si == "x":
#   continue
# else:
#   print("わからない")
# 求めるのはパターン数

"""
5月29日
階上の計算がよくわからない
?の扱いがよくわからない

"""