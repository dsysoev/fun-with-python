
class EvenOnly(list):
    def append(self, integer):
        if not isinstance(integer, int):
            raise TypeError("Only integers can be added")
        if integer % 2:
            raise ValueError("Only even numbers can be added")
        super().append(integer)

if __name__ in '__main__':

    lst = EvenOnly()

    for x in [2, 4, 8]:
        print('append {} to list'.format(x))
        lst.append(x)
        print('list: {}'.format(lst))

    x = 1
    print('insert {} to list'.format(x))
    lst.insert(0, x)
    print('list: {}'.format(lst))
    print('append {} to list'.format(x))
    lst.append(x)
    print('list: {}'.format(lst))
