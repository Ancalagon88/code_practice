def divider(n, k):
    i = 1
    multiplied = 0
    while multiplied < n:
        multiplied = k * i
        i += 1
    multiplied = multiplied - k
    remainder = n % k
    return (multiplied, remainder)


print(divider(5, 2))
