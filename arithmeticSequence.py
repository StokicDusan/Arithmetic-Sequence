from math import ceil

def arithmeticSequences(A: list,n:int = 0) -> list:
    '''
    arithmeticSequences(A,n) returns a list of lists of all arithmetic
    sequences from list A with common difference n OR all common
    differences if n = 0.
    An arithmetic sequence is valid only if it has more then 2 items.
    '''
    A.sort()
    SubSequence = []
    ArithmeticSequences = []
    # Create array of pairs from array A
    for index,item in enumerate(A[:-1]):
        for index2,item2 in enumerate(A[index+1:]):
            SubSequence.append([item,item2])
    # Finding arithmetic sequences
    if (n == 0):
        # if n is 0, find arithmetic sequences with all common differences
        for index,pair in enumerate(SubSequence):
            for commonDiff in range(1,ceil((A[-1]-A[0])/2)+1):
                if (pair[1] - pair[0] == commonDiff):
                    found = [pair[0],pair[1]]
                    for index2,pair2 in enumerate(SubSequence[index+1:]):
                        if (pair2[0] == found[-1] and pair2[1]-pair2[0] == commonDiff):
                            found.append(pair2[1])
                    if (len(found)>2): ArithmeticSequences.append(found)
    else:
        # if n is not 0, find arithmetic sequences common difference of n
        for index,pair in enumerate(SubSequence):
            if (pair[1] - pair[0] == n):
                found = [pair[0],pair[1]]
                for index2,pair2 in enumerate(SubSequence[index+1:]):
                    if (pair2[0] == found[-1] and pair2[1]-pair2[0] == n):
                        found.append(pair2[1])
                if (len(found)>2): ArithmeticSequences.append(found)
    return ArithmeticSequences

def distArSeq(A: list,n:int = 0) -> list:
    '''
    distArSeq(A,n) returns a list of lists of distinct arithmetic
    sequences from list A with common difference n OR all common
    differences if n = 0.
    distArSeq(A,n) returns a list that has no arithmetic sequences that
    are a subsequence of an existing sequence.
    An arithmetic sequence is valid only if it has more then 2 items.
    '''
    A.sort()
    seq = arithmeticSequences(A,n)
    DistinctArithmeticSequences = seq
    for index,item in enumerate(seq):
        for index2,item2 in enumerate([x for x in seq if x != item]):
            # Remove a sequence if it is a subsequence of an existing sequence
            if (set(item2) <= set(item)) and (item[1] - item[0] == item2[1] - item2[0]):
                DistinctArithmeticSequences.remove(item2)
    return DistinctArithmeticSequences

def test_arithmeticSequence() -> None:
    """
    >>> arSeq = [61,10,11,30,21,20,40,41,50,60,1,70]
    >>> distArSeq(arSeq)
    [[1, 11, 21], [1, 21, 41, 61], [10, 20, 30, 40, 50, 60, 70], [10, 30, 50, 70], [10, 40, 70], [20, 40, 60]]
    >>> distArSeq(arSeq,20)
    [[1, 21, 41, 61], [10, 30, 50, 70], [20, 40, 60]]
    >>> arSeq = [2,10,17,24,31,38,45,52,60]
    >>> distArSeq(arSeq)
    [[2, 31, 60], [10, 17, 24, 31, 38, 45, 52], [10, 24, 38, 52], [10, 31, 52], [17, 31, 45]]
    >>> distArSeq(arSeq,7)
    [[10, 17, 24, 31, 38, 45, 52]]
    >>> arSeq = [1,10,30,40,80,110]
    >>> distArSeq(arSeq)
    []
    """
    pass

if __name__ == "__main__":
    from doctest import testmod
    testmod()
