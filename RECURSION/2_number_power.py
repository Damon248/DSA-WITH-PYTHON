def num_pow(num, pow):
    # BC
    if pow == 1:
        return num
    if pow == 0:
        return 1

    # IH
    smallOp = num_pow(num, pow-1)

    # IS
    if smallOp == 1:
        return 1
    else:
        return num * smallOp


print(num_pow(5, -1))
