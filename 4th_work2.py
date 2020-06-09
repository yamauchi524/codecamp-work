# coding:utf-8

#0～2のランダムな数値を2つ取得
#「それぞれの数値」と「どちらの数値のほうが大きいか」の情報を表示

# 0〜2のランダムな数値を2つ取得し、それぞれ変数rand1とrand2へ代入
import random
rand1 = random.randint(0,2)
rand2 = random.randint(0,2)
 
# ランダムな数値rand1とrand2をそれぞれ表示
print('rand1: ', rand1)
print('rand2: ', rand2)

# rand1とrand2のどちらのほうが大きいか比較し、結果を表示
if rand1 > rand2:
    print('rand1の方が大きい値です')
elif rand1 < rand2:
    print('rand2の方が大きい値です')
else:
    print('2つは同じ値です')