"""
https://atcoder.jp/contests/abc202/tasks/abc202_a
"""

a, b, c = list(map(int, input().split())) #3つの文字で入力を受け取る


"""
反対側の面は(7-?)で求めることができる
"""

ans = (7-a) + (7-b) + (7-c)


print(ans)


"""
提出情報
提出日時	2021-05-24 13:04:12
問題	A - Three Dice
ユーザ	OrcaDive_U
言語	Python (3.8.2)
得点	100
コード長	125 Byte
結果	
実行時間	24 ms
メモリ	9156 KB
"""