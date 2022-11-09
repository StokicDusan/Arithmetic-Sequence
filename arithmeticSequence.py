def arithmeticSequence(A,n):
    SubSequence=[]
    ArithmeticSequences=[]
    #Create array of pairs from array A
    for index,item in enumerate(A[:-1]):
        for index2,item2 in enumerate(A[index+1:]):
            SubSequence.append([item,item2])
    #finding arithmetic sequences
    for index,pair in enumerate(SubSequence):
        if (pair[1] - pair[0] == n):
            found = [pair[0],pair[1]]
            for index2,pair2 in enumerate(SubSequence[index+1:]):
                if (pair2[0]==found[-1] and pair2[1]-pair2[0]==n):
                    found.append(pair2[1])
            if (len(found)>2): ArithmeticSequences.append(found)
    return ArithmeticSequences