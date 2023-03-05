def fact(n):

    # BC
    if n == 0:
        return 1

    # IH
    smallOp = fact(n-1)

    # IS
    return n * smallOp


n = int(input())
print(fact(n))
