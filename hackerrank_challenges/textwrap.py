'''
frase = input()
parag = int(input())
begin = 0
end = parag
comprimento = len(frase)
while comprimento > 0:
    print(frase[begin:end])
    comprimento -= parag
    begin += parag
    end += parag
'''

import textwrap

def wrap(string, max_width):
    wrapresult = textwrap.fill(string,max_width)
    return wrapresult

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)