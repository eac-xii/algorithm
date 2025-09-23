def counting_sort(DATA, TEMP, k):
    # DATA [] -- 입력 배열 (0 to k)
    # TEMP [] -- 정렬된 배열
    # COUNTS [] -- 카운트 배열
    
    COUNTS = [0] * (k + 1)
    
    for i in range(0, len(DATA)):
        COUNTS[DATA[i]] += 1
    print(COUNTS)
        
    for i in range(1, k + 1):
        COUNTS[i] += COUNTS[i - 1]
    print(COUNTS)
    
    for i in range(len(TEMP) - 1, -1, -1):
        COUNTS[DATA[i]] -= 1
        TEMP[COUNTS[DATA[i]]] = DATA[i]
    print(COUNTS)
        
arr = [0, 4, 1, 3, 1, 2, 4, 1]
tmp = [0] * len(arr)
counting_sort(arr, tmp, 5)
print(tmp)


# Counting Sort는 "비교하지 않는 정렬 알고리즘" O(n + k), k는 값의 최댓값

# (1) 빈도 세기
# (2) 누적합 구하기
#       값 i 이하의 숫자가 배열에 몇 개 있는가,
#       이 값이 바로 i값이 들어갈 마지막 인덱스 + 1
# (3) 뒤에서부터 원래 배열을 읽으며 TEMP에 넣기
#       안정성(stability)보장,
#       각 값이 들어갈 "마지막 자리"를 하나씩 줄여가면 채운 것.