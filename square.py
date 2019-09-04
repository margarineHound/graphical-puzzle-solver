from collections import deque

# verify ensures sanity of square objects
def verify(square):
    if isinstance(square, list):
        print('you have input a list')
    else:
        print('Incorrect input format')
        raise SystemExit
    if len(square) == 9:
        pass
    else:
        print("Incorrect input size")
        raise SystemExit

# check ensures sanity of square objects
def check(square):
    rotate_n = 0
    new_list = []
    for item in square:
        if item['top'] is 'b':
            rotate_n = 1
        if item['top'] is 'c':
            rotate_n = 2
        if item['top'] is 'd':
            rotate_n = 3
        new_list.append(sqr_rotate(item, rotate_n))
    return new_list

# sqr_rotate performs n rotations on dict1 (clockwise: top -> rht, rht -> btm, btm -> left, left -> top)
def sqr_rotate(dict1, n):
    new_dict_values = deque(dict1.values())
    print(f""" 
    ***********************************
    ***********************************
    BEFORE ROTATION:

            ---{dict1['top']}----
            |      | 
            {dict1['lft']}  1  {dict1['rht']} 
            |      |
            ---{dict1['btm']}---
     ***********************************
     ***********************************       
    """)
    new_dict_values.rotate(n)

    print(f""" 

    AFTER ROTATION:

            ---{dict1['top']}----
            |      | 
            {dict1['lft']}  1  {dict1['rht']} 
            |      |
            ---{dict1['btm']}---


    """)
    return dict(zip(dict1.keys(), new_dict_values))