import random


# Comparator
class IComparer:
    def compare(self, x, y) -> int:
        pass


class Sort:
    def sort(self, data: [], comparer: IComparer):
        pass


# Strategy
class MergeSortStrategy(Sort):
    def sort(self, data: [], comparer: IComparer):
        if len(data) < 2:
            return data[:]
        else:
            middle = int(len(data) / 2)
            left = self.sort(data[:middle], comparer)
            right = self.sort(data[middle:], comparer)
            return self._merge(left, right, comparer)

    def _merge(self, left, right, comparer):
        result = []
        i, j = 0, 0
        while i < len(left) and j < len(right):
            if comparer.compare(left[i], right[j]) > 0:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        while i < len(left):
            result.append(left[i])
            i += 1
        while j < len(right):
            result.append(right[j])
            j += 1
        return result


class Container:
    def __init__(self):
        self._strategy = None
        self._cont = []

    # Prototype
    def clone(self):
        cont = Container()
        cont._strategy = cont._strategy
        cont._cont = self._cont.copy()
        return cont

    def set_sort_strategy(self, sort_strategy: Sort):
        self._strategy = sort_strategy

    def execute_sort(self, comp: IComparer):
        self._cont = self._strategy.sort(self._cont, comp)

    def add(self, data):
        self._cont.append(data)

    def __str__(self):
        st = []
        for a in self._cont:
           st.append("[" + str(a) + "]")

        return ", ".join(st)


class BankAccount:
    def __init__(self, dollar, euro, rub):
        self.dollar = dollar
        self.euro = euro
        self.rub = rub

    def calc_sum(self):
        return self.dollar * 70 + self.euro * 80 + self.rub

    def __str__(self):
        return str(self.dollar) + "$, " + str(self.euro) + "€, " + str(self.rub) + "₽ : " + str(self.calc_sum()) + "₽"


class BankAccountComparator(IComparer):

    def compare(self, x, y) -> int:
        return x.calc_sum() - y.calc_sum()


if __name__ == '__main__':
    cont = Container()
    for a in range(13):
        cont.add(BankAccount(random.randrange(0, 100), random.randrange(0, 200), random.randrange(0, 1000)))
    print('==============')
    print(cont)
    print('==============')
    cont.set_sort_strategy(MergeSortStrategy())
    cont.execute_sort(BankAccountComparator())
    print(cont)
    print('==============')
