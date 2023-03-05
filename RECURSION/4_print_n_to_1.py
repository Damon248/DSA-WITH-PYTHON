def print_n_to_1(n):

    # BC
    if n == 0:
        return

    # IS
    print(n)

    # IH
    print_n_to_1(n-1)


print_n_to_1(7)
