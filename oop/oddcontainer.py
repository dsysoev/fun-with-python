
class OddContainer:
    def __contains__(self, x):
        if not isinstance(x, int) or not x % 2:
            return False
        return True

if __name__ in '__main__':

    container = OddContainer()

    for x in [1, 2, 1.]:
        print('{} in container: {}'.format(x, x in container))
