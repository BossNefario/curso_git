my_list = []
entradas = 5
while entradas > 0:
    my_list.append(int(input()))
    entradas -= 1
my_list.sort()
print(my_list)
print(my_list[-1])
my_list.pop(-1)
print(my_list)
for item in my_list:
    print(f'Lista no index {my_list.index(item)} é {item}')
print(len(my_list))
    
