
def balance(weights, left, right):
    totalLeft = 0
    totalRight = 0
    for i in left:
        totalLeft += weights[i]
    for i in right:
        totalRight += weights[i]

    if totalLeft < totalRight:
        return -1
    elif totalLeft > totalRight:
        return 1
    else:
        return 0

def test(weights, answer):
    test0 = balance(weights, [0,1,2,3], [4,5,6,7])

    if test0 == 0:
        # remaining 8,9,10,11
        test1 = balance(weights, [8,9], [10, 0])
        if test1 == 0:
            return 11
        test2 = balance(weights, [9], [8])
        if test2 == test1:
            return 9
        if test2 == -test1:
            return 8
        return 10

    # remaining 0,1,2,3,4,5,6,7
    test1 = balance(weights, [0,1,4], [2,3,5])
    if test1 == test0:
        # remaining 0,1,5
        test2 = balance(weights, [0], [1])
        if test2 == test0:
            return 0
        if test2 == -test0:
            return 1
        return 5

    if test1 == -test0:
        # remaining 2,3,4
        test2 = balance(weights, [2], [3])
        if test2 == test0:
            return 2
        if test2 == -test0:
            return 3
        return 4

    #remaining 6,7
    test2 = balance(weights, [6], [11])
    if test2 == 0:
        return 7
    return 6

def main():
    for i in xrange(12):
        weights = [1] * 12
        weights[i] = 1.5
        result = test(weights, i)
        print str(weights) + " Result " + str(result)
        if result != i:
            print "Test " + str(i) + " too heavy failed with result " + str(result)

        weights[i] = 0.5
        result = test(weights, i)
        print str(weights) + " Result " + str(result)
        if result != i:
            print "Test " + str(i) + " too light failed with result " + str(result)

    print "DONE"

main()
