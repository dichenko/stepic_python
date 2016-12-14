
with open('input7.txt') as f:
    data = f.readlines()

for i in range(len(data)):
    data[i] = data[i][:-1]


def obrabotka1(m):
    """
    принимаем на вход строку, режем по скобкам, возвращаем список
    :param m:
    :return: list_
    """
    a = []
    while len(m) > 0:
        s = ''
        while len(m) > 0 and m[0] != '[':
            s += m[0]
            m = m[1:]
        m = m[1:]
        a.append(s)
        s = ''
        while len(m) > 0 and m[0] != ']':
            s += m[0]
            m = m[1:]
        a.append(s)
        m = m[1:]

    return a[:-1]

def there_is_abba_in_str(s):
    """
    ищем abba во входящей строке
    :param s:
    :return:
    """
    flag = False
    for i in range(len(s)-3):
        if s[i] == s[i+3] and s[i+1]==s[i+2] and s[i] != s[i+1]:
            flag = True

            break
    return  flag


def there_is_tls_in_big_str(d):
    flag1 = False  # Ищем аббу в скобках
    for i in range(1, len(d), 2):
        if there_is_abba_in_str(d[i]):
            flag1 = True
            break
    if flag1:

        return False
    else:

        flag2 = False
        for i in range(0, len(d), 2):

            if there_is_abba_in_str(d[i]):
                flag2 = True
                break
        return flag2




counter = 0

for i in range(len(data)):
    data[i] = obrabotka1(data[i])
    if len(data[i]) % 2 < 1: print(len(data[i]))
    if there_is_tls_in_big_str(data[i]):
        print(data[i])
        counter += 1



print(counter)