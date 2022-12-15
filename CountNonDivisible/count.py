def solution(A):
    m=max(A)
    R = []
    NonDivUni = {}
    counts = [0] * (m+1)

    for a in A:
        counts [a]+=1

    AA = set(A)
    for a in AA:
        s=0
        for j in range (1,int(a**0.5)+1):
            if a%j==0:
                s+=counts[j]
                if(int(a/j)!=j):
                    s+=counts[int(a/j)]
        NonDivUni[a]=(len(A)-s)

    for a in A:
        R.append(NonDivUni)

    return R