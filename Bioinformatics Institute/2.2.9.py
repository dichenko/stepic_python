#k = int(input())
#n = int(input())

def refact(k):
    """
    Принимает на вход int k и обрабатывает её по алгоритму.
    :param int k:
    :return: int k
    """
    k = str(k)
    s = ''
    i = 0
    while len(k) > 0:
        if k[i] != k[i+1]:
            s += '1'
            s += k[i]
            k = k[1:]
            i+=1
            print('s = ',s)
        else:
            counter = 0
            while k[i] == k[i+1]:
                counter += 1
                k = k[1:]
            s += str(counter)
            s += k[i]
            i += 1

            print('s = ', s)

    return int(s)


def good_ans(k):
    """
    Переводит целое число в формат ответа
    :param int k:
    :return: str k
    """
    k = str(k)
    k1 = ''
    for el in k:
        k1+= el
        k1 += ' '
    return k1[:-1]

def foo(k,n):
    if n == 1: return k
    else:
        for i in range(n):
            k = refact(k)
    return good_ans(k)




print(refact(11222555))