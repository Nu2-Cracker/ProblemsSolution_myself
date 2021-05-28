#https://atcoder.jp/contests/abc202/tasks/abc202_b

s = input()

#反転する
#6=>7=>9
#9=>5=>6
s = s[::-1].replace("6", "7").replace("9", "5").replace("7", "9").replace("5", "6")
#5,7は含まれないため
print(s)


"""
提出情報
提出日時	2021-05-28 10:12:29
問題	B - 180°
ユーザ	OrcaDive_U 
言語	Python (3.8.2)
得点	200
コード長	145 Byte
結果	
実行時間	29 ms
メモリ	9004 KB

"""