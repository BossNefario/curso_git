n = int(input())
while n > 0:
    x = int(input())
    if x % 2 == 0 and x > 0:
        print('EVEN POSITIVE')
    elif x % 2 == 0 and x < 0:
        print('EVEN NEGATIVE')
    elif x % 2 != 0 and x < 0:
        print('ODD NEGATIVE')
    elif x % 2 != 0 and x > 0:
        print('ODD POSITIVE')
    else:
        print('NULL')
    n -= 1
