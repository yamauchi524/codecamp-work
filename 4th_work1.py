# coding:utf-8

import random
rand = random.randint(1,6)

#でた数字を表示
#偶数か奇数か

print('number:',rand)

if rand % 2 == 0 :
    print('偶数')
else:
    print('奇数')