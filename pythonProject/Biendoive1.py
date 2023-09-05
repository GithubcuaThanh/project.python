while True:
    N = int(input())
    if N == 0:
        break
    count = {N: 1}
    while N != 1:
        if N%2 == 0:
            N = int(N/2)
        else:
            N = N*3 + 1
        if N not in count:
            count[N] = 1
    print(len(count))