
def utest_find_closest_sum(func):
    assert func([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0]) == 0
    assert func([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [-1]) == 0
    assert func([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [11]) == 45
    assert func([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [5]) == 15
    assert func([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [-10, 10]) == 45
    assert func([-10, -9, -8, -7, -6, -5, -4, -3, -2, -1], [-11]) == -10
    assert func([-10, -9, -8, -7, -6, -5, -4, -3, -2, -1], [10]) == -55
    assert func([-10, -9, -8, -7, -6, -5, -4, -3, -2, -1], [-5]) == -45
    assert func([100, 0, 1], [100, -1]) == 101
    assert func([100, 0, 1], [100, 10]) == 102
    assert func([10, 1, -1, 0], [-1, 100]) == 9

from find_closest_sum import find_closest_sum1

def test_find_closest_sum1():
    utest_find_closest_sum(find_closest_sum1)

from find_closest_sum import generate_lists

lst_values, lst_targets = generate_lists(int(1e4))

from find_closest_sum import find_closest_sum1

def test_performance1():
    find_closest_sum1(lst_values, lst_targets)
    

from find_closest_sum import find_closest_sum2

def test_find_closest_sum2():
    utest_find_closest_sum(find_closest_sum2)
    
def test_performance2():
    find_closest_sum2(lst_values, lst_targets)

from find_closest_sum import find_closest_sum3

def test_find_closest_sum3():
    utest_find_closest_sum(find_closest_sum3)
    
def test_performance3():
    find_closest_sum3(lst_values, lst_targets)
