#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random


def confusion_matrix(bloomfilter, size, low=0, prob=0.5, random_state=None):
        
    random.seed(random_state)
    num_list = set(map(str, range(low, low + size)))
    seen_list = {x for x in num_list if random.random() < prob}
    
    for x in seen_list:
        bloomfilter.add(x)
        
    true = (x in seen_list for x in num_list)
    pred = (x in bloomfilter for x in num_list)

    results = {}
    for t, p in [(True, True), (True, False), (False, True), (False, False)]:
        results[(t, p)] = 0

    for t, p in zip(true, pred):
        results[(t, p)] += 1
        
    return results, bloomfilter

def accuracy(results):
    return (results[(True, True)] + results[False, False]) / (sum(results.values()))

def precision(results):
    return results[(True, True)] / (results[(True, True)] + results[False, True])

def recall(results):
    return results[(True, True)] / (results[(True, True)] + results[True, False])

def pretty_print(results):
    print('          True     False')
    print('Positive  {:<8d} {:<8d}'.format(results[(True, True)], results[(False, True)]))
    print('Negative  {:<8d} {:<8d}'.format(results[(True, False)], results[(False, False)]))
    print('accuracy  : {:.4f}'.format(accuracy(results)))
    print('precision : {:.4f}'.format(precision(results)))
    print('recall    : {:.4f}'.format(recall(results)))
