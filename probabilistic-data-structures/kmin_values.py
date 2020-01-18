#!/usr/bin/env python
# -*- coding: utf-8 -*-

import mmh3
import blist


class KMinValues(object):

    def __init__(self, num_hashes):
        self.num_hashes = num_hashes
        self.data = blist.sortedset()

    def add(self, item):
        item_hash = mmh3.hash(item)
        self.data.add(item_hash)
        if len(self.data) > self.num_hashes:
            self.data.pop()

    def __len__(self):
        if len(self.data) < self.num_hashes:
            return len(self.data)
        value = (self.num_hashes - 1) * (2 ** 32 - 1) / \
            float(self.data[-2] + 2 ** 31 - 1)
        return int(value)
