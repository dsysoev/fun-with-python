
import random

def generate_lists(n):
    return [random.randint(0, n) for _ in range(n)], [random.randint(-n - 1, n + 1) for _ in range(n)]

def find_closest_sum1(vlst, tlst):
    
    # sort
    vlist = sorted(vlst)
    
    targets = []
    for target in tlst:
        vmin = float('Inf')
        closest = None
        for i in range(len(vlist)):
            value = abs(vlist[i] - target)
            if value <= vmin:
                vmin = value
                closest = i

        targets.extend(vlist[:closest + 1])
        
    return sum(targets)

import bisect


def find_closest_sum2(vlst, tlst):
    
    # list should be sorted
    vlist = sorted(vlst)
    
    targets = []
    for target in tlst:
        # bisect.bisect_left will return the first value in the list
        # that is greater than or equal to the target
        i = bisect.bisect_left(vlist, target)
        
        if i == len(vlist):
            indx = i - 1
        elif vlist[i] == target:
            indx = i
        elif i > 0:
            j = i - 1
            # since we know value is larger than target 
            # (and vice versa for the value at j),
            # we don't need to use absolute values here
            if vlist[i] - target > target - vlist[j]:
                indx = j
        else:
            indx = i
        
        targets.extend(vlist[:indx + 1])
            
    return sum(targets)

import bisect


def find_closest_sum3(vlst, tlst):
    
    # list should be sorted
    vlist = sorted(vlst)
    
    # create hash for store target results
    hash_map = {}
    
    vsum = 0
    targets = []
    for target in tlst:
        # bisect.bisect_left will return the first value in the list
        # that is greater than or equal to the target
        i = bisect.bisect_left(vlist, target)
        
        if i == len(vlist):
            indx = i - 1
        elif vlist[i] == target:
            indx = i
        elif i > 0:
            j = i - 1
            # since we know value is larger than target 
            # (and vice versa for the value at j),
            # we don't need to use absolute values here
            if vlist[i] - target > target - vlist[j]:
                indx = j
        else:
            indx = i
        
        if target not in hash_map:
            hash_map[target] = sum(vlist[:indx + 1])
        
        vsum += hash_map[target]
            
    return vsum
