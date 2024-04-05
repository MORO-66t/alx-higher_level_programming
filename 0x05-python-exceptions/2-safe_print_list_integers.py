#!/usr/bin/python3
def safe_print_list_integers(my_list=[1,1,14,'m', 1.22], x=5):
    i, c = 0, 0
    while i < x:
        try:
            print("{:d}".format(my_list[i]), end='')
            c += 1
        except (ValueError, TypeError):
            pass
        i += 1
    print()
    return


safe_print_list_integers()
    