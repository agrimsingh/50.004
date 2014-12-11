"""
__author__ = "agrim singh"
__id__ = "1000748"
"""
import sys
    ############## WRITE YOUR CODE HERE #####################
    ############## You can also write your only code without using this file #####################
def knapsack(items, maxweight):
    """
    Using top down DP to solve knapsack problem by finding the most valuable
    subsequence of 'items' that weigh at most as 'maxweight'.
    
    'items' is a sequence of (value, weight) pairs where value is a number
    and weight is a non-negative integer. 'maxweight' is non-negative as well.

    Program returns a pair whose first element is the most valuable seq of 'items'
    and second element is the subsequence.

    >>> items = [(3, 9), (2, 2), (5, 4), (1, 1), (6, 3)]
    >>> knapsack(items, 13)
    (14, [(2, 2), (5, 4), (1, 1), (6, 3)])

    Values are pushed to bestTotalValue and itemsToUse in __main__ to display.
    """
    def bestvalue(i, j):
        if i == 0: return 0 #base case
        value, weight = items[i - 1]
        if weight > j:
            return bestvalue(i - 1, j)
        else:
            return max(bestvalue(i - 1, j),
                       bestvalue(i - 1, j - weight) + value)

    j = maxweight
    result = []
    for i in xrange(len(items), 0, -1):
        if bestvalue(i, j) != bestvalue(i - 1, j):
            result.append(items[i - 1])
            j -= items[i - 1][1]
    result.reverse()
    return bestvalue(len(items), maxweight), result

#pre-defined main method 
if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('usage: knapsack.py [file]')
        sys.exit(1)

    filename = sys.argv[1]
    with open(filename) as f:
        lines = f.readlines()

    maxweight = int(lines[0])
    items = [map(int, line.split()) for line in lines[1:]]

    bestTotalValue, itemsToUse = knapsack(items, maxweight)

    print('Best possible total value: {0}'.format(bestTotalValue))
    print('Items:')
    for value, weight in itemsToUse:
        print('Value: {0}, Weight: {1}'.format(value, weight))
