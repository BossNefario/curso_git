if __name__ == '__main__':
    n = int(input())
    integer_list = tuple(map(int, input().split()))
    hash_integer_lista = hash(integer_list)
    print(hash_integer_lista)
