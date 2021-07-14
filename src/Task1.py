
class Count:
    def __init__(self):

        p1 = "Введите количество товаров:"

        p2 = "Введите количсетво рублей:"

        p3 = "Введите количсетво копеек:"

        self.proposals = [p1, p2, p3]

        self.data = []

        self.i = 0

    def count(self):
        for self.proposal in self.proposals:
            self._verify()

        s, m, n = (self.data[k] for k in range(len(self.data)))
        price = s * m + (s * n)//100 + ((s * n) % 100)/100
        print("Конечная цена: %.2f. рублей" % price)

    def _verify(self):
        while True:
            number = input(self.proposal)
            try:
                number = int(number)
                self.data.append(number)
                self.i += 1
                break
            except ValueError:
                print("Нужно ввести целое число!")
                continue


if __name__ == '__main__':
    MyCount = Count()
    MyCount.count()
