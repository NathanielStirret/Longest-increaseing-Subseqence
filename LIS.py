def lis(arr):
    n = len(arr)
    if n == 0:
        return 0

    mem = [1] * n   # this is our memory

    # Fill the memeory
    for i in range(1, n):
        for j in range(i):
            if arr[j] < arr[i]:
                # save the best result so far
                mem[i] = max(mem[i], mem[j] + 1)

    # The answer is the maximum saved value
    return max(mem)
