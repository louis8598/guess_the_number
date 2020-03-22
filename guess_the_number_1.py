import random
r = random.randint(1, 5)
number = 3
while number > 0:
    number = number - 1
    k = input('請3次內從1-5猜中一個數字:')
    k = int(k)
    if k == r:
        print('正確答案!!')
        break
    else:
        print('猜錯了~')
        if number > 0:
            print('你還有', number,'次機會')
        else:
            print('你輸了!!')
            break
