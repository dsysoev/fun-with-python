class Silly:
    @property
    def silly(self):
        "This is a silly property"
        print("You are getting silly")
        return self._silly

    @silly.setter
    def silly(self, value):
        print("You are making silly {}".format(value))
        self._silly = value

    @silly.deleter
    def silly(self):
        print("Whoah, you killed silly!")
        del self._silly

if __name__ in '__main__':
    silly = Silly()
    print('set silly = 1')
    silly.silly = 1
    print('get silly: {}'.format(silly.silly))
    print('delete silly')
    del silly.silly
    print('get silly: {}'.format(silly.silly))
