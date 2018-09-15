
class LongNameDict(dict):
    def longest_key(self):
        longest = None
        for key in self:
            if not longest or len(key) > len(longest):
                longest = key
        return longest

if __name__ in '__main__':

    longdict = LongNameDict({
        'a': 1,
        'ab': 2,
        'abc': 3
        })

    print(longdict)
    print(longdict.longest_key())
