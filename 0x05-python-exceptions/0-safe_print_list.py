def safe_print_list(my_list=[], x=0):
    i = 0

    while i < x:
        try:
            print(my_list[i])

        except IndexError:

            break
        i += 1
