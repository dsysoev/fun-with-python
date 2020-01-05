
import string
import bisect
import dawg
import marisa_trie
import hat_trie
import datrie


def load_as_list(filepath):
    
    with open(filepath, 'r') as f:
        data = [x.rstrip() for x in f.readlines()]
    return data


def load_as_set(filepath):
    
    with open(filepath, 'r') as f:
        data = {x.rstrip() for x in f.readlines()}
    return data


def bisect_index(a, x):
    i = bisect.bisect_left(a, x)
    if i != len(a) and a[i] == x:
        return i
    return -1


def load_as_dawg(filepath):
    
    with open(filepath, 'r') as f:
        data = dawg.DAWG(x.rstrip() for x in f.readlines())
    return data


def load_as_marisatrie(filepath):
    
    with open(filepath, 'r') as f:
        data = marisa_trie.Trie(x.rstrip() for x in f.readlines())
    return data


def load_as_hattrie(filepath):
    
    with open(filepath, 'r') as f:
        data = hat_trie.Trie()
        for x in f.readlines():
            data[x.rstrip()] = 0
    return data


def load_as_datrie(filepath):

    with open(filepath, 'r') as f:
        lines = (x.rstrip() for x in f.readlines())
    
    data = datrie.Trie(string.printable)
    for x in lines:
        data[x] = 0
    return data
