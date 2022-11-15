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

def distinctArithmeticSequences(A):
    DistinctArithmeticSequences = A
    for index,item in enumerate(A):
        for index2,item2 in enumerate([x for x in A if x != item]):
            if (set(item2) <= set(item)):
                DistinctArithmeticSequences.remove(item2)
    return DistinctArithmeticSequences

def main():
    df = [1,10,11,20,21,30,40,41,50,60,61,70]
    common_differene=10

    arseq=arithmeticSequence(df,common_differene)
    print(arseq)

    darseq=distinctArithmeticSequences(arseq)
    print(darseq)

if __name__ == "__main__":
    main()
