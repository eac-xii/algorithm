def f(i, N): # i 배열 인덱스, N 배열크기
    if i == N: # 중단 조건
        return
    else: # 재귀 호출
        print(A[i])
        f(i + 1, N)

A = [1, 2, 3]
f(0, 3)