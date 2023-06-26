#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    int = 0
    while int < x:
        try:
            print(my_list[int], end="")
            int += 1
        except IndexError:
            break
    print('')
    return (int)
