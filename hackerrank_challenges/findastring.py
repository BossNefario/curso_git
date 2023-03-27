def count_substring(string, sub_string):
    contagem = 0
    for i in range(len(string)):
        if sub_string == string[i:len(sub_string) + i]:
            contagem += 1
    return contagem

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    count = count_substring(string, sub_string)
    print(count)