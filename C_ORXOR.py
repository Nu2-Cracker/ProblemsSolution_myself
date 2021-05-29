# https://atcoder.jp/contests/abc197/tasks/abc197_c



N = int(input())
val = list(map(int, input().split(" ")))


def calc_or(list_):
  """
  or演算を計算する
  """
  or_ = 0
  for i in list_:
    or_ |= i
  return or_

def calc_xor_min(cutlist):
  """
  xor演算子を計算する。
  """
  res = 0
  for val in cutlist:
    res ^= calc_or(val)
  return res




res=0
for i in range(1,N):
  cutlist = [val[:i], val[i:]]
  xor = calc_xor_min(cutlist)
  if i==1: #初期値のみ
    res = xor
  else:
    if res > xor: #②回目以降は、resよりxorが小さい場合のみxorを更新
      res = xor

print(res)




"""
提出情報
提出日時	2021-05-29 23:33:43
問題	C - ORXOR
ユーザ	OrcaDive_U 
言語	Python (3.8.2)
得点	0
コード長	617 Byte
結果	
実行時間	23 ms
メモリ	9184 KB
ジャッジ結果
セット名	Sample	All
得点 / 配点	0 / 0	0 / 300
結果	
× 3
× 15
× 12
セット名
"""