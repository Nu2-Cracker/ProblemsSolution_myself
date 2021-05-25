# https://atcoder.jp/contests/abc201/tasks/abc201_a


nums = list(map(int, input().split()))

"""
小さい順に並び替えて確かめる??
"""
#昇順にソート
#今回のケースでは必要ない
# def bubble_sort(nums):
#   for i in range(len(nums)-1):
#     #列の先頭2要素を最初の比較対象に選ぶ
#     l = 0
#     r = 1

#     #rが末尾に達するまで、隣り合う要素の大小を比較する
#     while r < len(nums):
#       #隣あう要素の大小が逆であれば交換する
#       if nums[l] > nums[r]:
#         nums[l], nums[r] = nums[r], nums[l]
#       #比較対象のindexをインクリメンとする
#       l += 1
#       r += 1

#     return nums




nums.sort()
ans = "No"
if (nums[2] - nums[1]) == (nums[1] - nums[0]):
  ans = "Yes"

print(ans)

"""
1回目
提出情報
提出日時	2021-05-25 09:04:46
問題	A - Tiny Arithmetic Sequence
ユーザ	OrcaDive_U
言語	Python (3.8.2)
得点	0
コード長	729 Byte
結果
実行時間	25 ms
メモリ	9148 KB
ジャッジ結果
セット名	Sample	All
得点 / 配点	0 / 0	0 / 100
結果
× 3
× 10

問題文読もう
ダメらしい

バブルソートダメらしい
"""

"""
提出情報
提出日時	2021-05-25 09:15:32
問題	A - Tiny Arithmetic Sequence
ユーザ	OrcaDive_U 
言語	Python (3.8.2)
得点	100
コード長	800 Byte
結果	
実行時間	30 ms
メモリ	9100 KB
ジャッジ結果
セット名	Sample	All
得点 / 配点	0 / 0	100 / 100
結果	
× 3
× 10

pythonの標準のソート使っちゃダメなんてルールはないよね
"""