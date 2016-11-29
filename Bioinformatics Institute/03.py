class Buffer:
    def __init__(self):
        self.b = []

    def add(self, *a):
        for el in a:
            self.b.append(el)
        while len(self.b) >= 5:
            x = self.b
            y = x[:5]
            su = 0
            for el in y:
                su += el
            self.b = x[5:]
            print(su)

    def get_current_part(self):
        print (*self.b)

buf = Buffer()
buf.add(1, 2, 3)
buf.get_current_part() # вернуть [1, 2, 3]
buf.add(4) # print(15) – вывод суммы первой пятерки элементов
buf.add(4,9)
buf.get_current_part() # вернуть [6]
buf.add(7, 8, 9, 10) # print(40) – вывод суммы второй пятерки элементов
buf.get_current_part() # вернуть []
buf.add(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,1,1,1) # print(5), print(5) – вывод сумм третьей и четвертой пятерки
buf.get_current_part() # вернуть [1]