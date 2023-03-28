i = 1
j = 7
while i != 11:
    if j == 7:
        print(f'I={i} J={j}')
        j -= 1
    elif j == 6:
        print(f'I={i} J={j}')
        j -= 1
    elif j == 5:
        print(f'I={i} J={j}')
        j += 2
        i += 2
    else:
        break
    

