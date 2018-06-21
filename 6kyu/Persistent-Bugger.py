def persistence(n):
    product = 1
    if n < 10:
        return 0
    for i in str(n):
        product *= int(i)
    return 1 + persistence(product)