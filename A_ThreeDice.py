"""
https://atcoder.jp/contests/abc202/tasks/abc202_a
"""

a, b, c = input().split() #3つの文字で入力を受け取る

res = list(map(int,[a, b, c]))

dice = [(1, 6), (2, 5), (3, 4)] #ダイスはタプルの組として扱う

sum_ = 0
for i in res:
  for d, r in dice: #一致する要素を全探索する
    if i == d: #当てはまったら逆の要素を足す
      sum_ += r
    elif i == r:
      sum_ += d


print(sum_)

"""
提出情報
提出日時	2021-05-24 12:56:53
問題	A - Three Dice
ユーザ	OrcaDive_U 
言語	Python (3.8.2)
得点	100
コード長	394 Byte
結果	
実行時間	28 ms
メモリ	8988 KB
"""