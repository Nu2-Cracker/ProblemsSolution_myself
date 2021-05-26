# https://atcoder.jp/contests/abc200/tasks/abc200_b

N, K  = list(map(int, input().split()))

for _ in range(K):
  if N % 200 == 0:
    N /= 200
  else:
    N = str(int(N)) + "200"
    N = int(N)

print(int(N))

"""
提出情報
提出日時	2021-05-26 19:36:11
問題	B - 200th ABC-200
ユーザ	OrcaDive_U 
言語	Python (3.8.2)
得点	200
コード長	168 Byte
結果	
実行時間	28 ms
メモリ	9132 KB
ジャッジ結果
セット名	Sample	All
得点 / 配点	0 / 0	200 / 200
結果	
× 3
× 21

"""