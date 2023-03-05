def print_1_to_n(n):

    # BC
    if n == 0:
        return

    # IH
    print_1_to_n(n-1)

    # IS
    print(n)
    return


print_1_to_n(10)
