#!/usr/bin/env python
# -*- coding: utf-8 -*-

import bitarray
import math
import mmh3
import random


class BloomFilter(object):

    def __init__(self, capacity, error=0.005):
        """
        Initialize a bloom filter with given capacity and false positive rate
        """
        self.capacity = capacity
        self.error = error
        self.num_bits = int(-capacity * math.log(error) / math.log(2) ** 2) + 1
        self.num_hashes = int(self.num_bits * math.log(2) / capacity) + 1
        self.data = bitarray.bitarray(self.num_bits)

    def _indexes(self, key):
        h1, h2 = mmh3.hash64(key)
        for i in range(self.num_hashes):
            yield (h1 + i * h2) % self.num_bits

    def add(self, key):
        for index in self._indexes(key):
            self.data[index] = True

    def __contains__(self, key):
        return all(self.data[index] for index in self._indexes(key))

    def _len(self):
        num_bits_on = self.data.count(True)
        if num_bits_on == self.num_bits:
            raise Exception('bloom filter is full')
        log = 1.0 - num_bits_on / self.num_bits
        return -1.0 * self.num_bits * math.log(log) / self.num_hashes
    
    def __len__(self):
        return int(self._len())
    
    def get_free_bits_ratio(self):
        return self.data.count(True) / self.num_bits

    @staticmethod
    def union(bloom_a, bloom_b):
        assert bloom_a.capacity == bloom_b.capacity, "Capacities must be equal"
        assert bloom_a.error == bloom_b.error, "Error rates must be equal"

        bloom_union = BloomFilter(bloom_a.capacity, bloom_a.error)
        bloom_union.data = bloom_a.data | bloom_b.data
        return bloom_union
    
