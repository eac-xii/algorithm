def fibo(n):
    global count
    count += 1
    if n < 2:
        return n
    else:
        return fibo(n - 1) + fibo(n - 2)

count = 0 # 호출 횟수 기록
print(fibo(10), count)