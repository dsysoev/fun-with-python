class ReadOnlyX:
    def __setattr__(self, attr, value):
        if attr == "x":
            raise AttributeError("X is immutable")
        super().__setattr__(attr, value)

if __name__ in '__main__':
    obj = ReadOnlyX()
    print('add y attribute = 10')
    obj.y = 10
    print('get y value: {}'.format(obj.y))
    print('add x attribute = 10')
    obj.x = 10
