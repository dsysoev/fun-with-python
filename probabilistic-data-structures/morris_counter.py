#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math
import array
import random


class MorrisCounter(object):

    def __init__(self, array_type=u'B', nbr_counters=1):
        self.exponents = array.array(array_type, [0] * nbr_counters)

    def __len__(self):
        return len(self.exponents)

    def add_counter(self):
        """Add a new zeroed counter"""
        self.exponents.append(0)

    def get(self, counter=0):
        """Calculate approximate value represented by counter"""
        return math.pow(2, self.exponents[counter])

    def add(self, counter=0):
        """Probabilistically add 1 to counter"""
        value = self.get(counter)
        probability = 1.0 / value
        if random.uniform(0, 1) < probability:
            self.exponents[counter] += 1
    
    def __str__(self):
        return str(self.get())
    
    def __repr__(self):
        return self.get()
        
