def sum_n(num):

    # BC
    if num == 1:
        return 1

    # IH
    smallOp = sum_n(num-1)

    # IS
    return num + smallOp


num = int(input())
print(sum_n(num))
