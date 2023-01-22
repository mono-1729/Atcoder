def query():
    N = int(input())
    A = list(map(int, input().split())) * 2
    B = list(map(int, input().split()))

    if A[:N] == B:
        return "Yes"

    B.append(B[0])
    m_B = []
    for n in range(N):
        if B[n] != B[n+1]:
            m_B.append(B[n])
    if len(m_B) == 0:
        m_B.append(B[0])

    if len(m_B) == N:
        return "No"

    for i in range(N):
        B_index = 0
        for j in range(N):
            if A[i+j] == m_B[B_index]:
                B_index += 1
                if B_index == len(m_B):
                    return "Yes"

    return "No"


T = int(input())
for t in range(T):
    print(query())
