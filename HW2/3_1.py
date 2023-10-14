# Copyright 2023 Jinzhi Shen jinzhis9@bu.edu
def show_integer_properties():
    Table = "{:<6} {:<22} {:<22} {:<22}"
    print(Table.format('Bytes','Largest Unsigned Int','Minimum Signed Int','Maximum Signed Int'))
    for i in range(1, 9):
        L_unsigned = 2**(8 * i) - 1
        min_signed = -2**(8 * i - 1)
        max_signed = 2**(8 * i - 1) - 1
        print(Table.format(i, L_unsigned, min_signed, max_signed))



show_integer_properties()
