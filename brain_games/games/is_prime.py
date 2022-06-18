def is_prime(end):
    list = []
    for i in range(2, end):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            list.append(i)
    return list
