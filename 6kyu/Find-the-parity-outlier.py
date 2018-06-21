def find_outlier(integers):
    if integers[0] % 2 != integers[1] % 2:
        return integers[0] if integers[2] % 2 == integers[1] % 2 else integers[1]
    for i in integers:
        if i % 2 != integers[0] % 2:
            return i