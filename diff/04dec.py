with open('input.txt') as f:
    data = f.readlines()


def ref(x):
    '''
    получает на вход строку, обрабатывает, возвращает список
    :param x:
    :return: [строка, ID, контрольная сумма]
    '''
    i = 0
    stroka = ''
    id_ = ''
    kontrol_sum = ''
    while i < len(x):
        if x[i] in '1234567890':
            break
        elif x[i] == '-':
            i += 1
        else:
            stroka += x[i]
            i += 1
    while x[i] in  '1234567890':
        id_+= x[i]
        i += 1
    kontrol_sum = x[i:-1]
    return [stroka, int(id_), kontrol_sum[1:-1]]


def most_common(s):
    """
    Принимает строку и возвращает строку самых састых букв в порядке убывания
    :param s:
    :return:
    """
    set_of_letters = set(s)
    li = []
    s1 = ''
    for el in set_of_letters:
        li.append([el, s.count(el)])
    li.sort(key = lambda x:( x[1], x[0]))
    li.sort(key = lambda x: x[1],reverse=True)

    for el in li:
        s1 += el[0]
    return s1[:5]

print(most_common('dddddffabc'))

for i in range(len(data)):
    data[i] = ref(data[i])


"""
data =
['fubrjhqlfedvnhwdftxlvlwlrq', 803, 'wjvzd']
['kzgwomvqkrmttgjmivlmxizbumvb', 902, 'zmnji']

"""

for i in range(len(data)):
    data[i][0] = most_common(data[i][0])

summa = 0
for i in range(len(data)):
    if data[i][0] == data[i][2]:
        print (data[i])
        summa += data[i][1]



print(summa)