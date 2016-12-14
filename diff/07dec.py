
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
    p = m.find('[')
    a.append(m[:p])
    l = m.find(']')
    a.append(m[p+1:l])
    a.append(m[l+1:])
    return a


def there_is_abba_in_str(s):
    """
    ищем abba во входящей строке
    :param s:
    :return:
    """
    flag = False
    for i in range(len(s)-3):
        if s[i] == s[i+3] and s[i+1]==s[i+2]:
            flag = True
            break
    return  flag

counter = 0

for i in range(len(data)):
    data[i] = obrabotka1(data[i])
    if not there_is_abba_in_str(data[i][1]):
        if there_is_abba_in_str(data[i][0]) or there_is_abba_in_str(data[i][2]):
            counter += 1
            print(data[i])


print(counter)