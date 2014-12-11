"""
Agrim Singh // 1000748 // 50.004 Introduction to Algorithms // Problem Set 1
"""
import math

def quick_find_1d_peak(a, i, j):
    #m = int(math.floor((i+j)/2))
    print "Looking at range: [", i, "", j, "]"
    m = (i + j) // 2
    print "Splitting on index", m, "= floor((", i, "+", j,") / 2)"
    if m >= 1 and a[m - 1] > a[m]:
        return quick_find_1d_peak(a, i, m - 1)
    elif m < len(a) - 1 and a[m] < a[m + 1]:
        return quick_find_1d_peak(a, m + 1, j)
    else: # a[m - 1] <= a[m] >= a[m + 1]
        return m;

v = [1, 2, 3, 3, 5, 1, 3]
#v = [1, 2, 4, 3, 5, 1, 3]
#v = [5, 4, 3, 2, 1]
#v = [5, 4, 3, 2]
#v = [1, 2, 3, 2, 1]
#v = [1, 2, 3, 2]

print "Finding a peak in", v
p = quick_find_1d_peak(v, 0, len(v) - 1)

print "1D peak found at a[",p,"] =", v[p]
