k = int(input())
n = int(input())

def refact(k):
    """
    Принимает на вход int k и обрабатывает её по алгоритму.
    :param int k:
    :return: int k
    """
    #print('_____run refact(', k,')' , end = ' ')
    k = str(k)
    s = ''
    if len (k) > 1:
        while len(k) > 0:
            if len(k) > 1 and k[0] != k[1]:
                s += '1'
                s += k[0]
                k = k[1:]
            else:
                counter = 0
                while len(k) > 1 and k[0] == k[1]:
                    counter += 1
                    k = k[1:]
                s += str(counter+1)
                s += k[0]
                k = k[1:]
        #print('s=',s)
        return int(s)
    else:
        return int('1'+str(k))



def good_ans(k):
    """
    Переводит целое число в формат ответа
    :param int k:
    :return: str k
    """
    k = str(k)
    k1 = ''
    for el in k:
        k1 += el
        k1 += ' '
    return k1[:-1]


def foo(k,n):
    #print('_____run foo', n, k)
    if n == 1:
        return k
    else:
        for i in range(1,n):
            k = refact(k)

    return good_ans(k)


print(foo(k,n))