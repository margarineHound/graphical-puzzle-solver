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

#TODO: Note that the "rotation" is not used in the printing. This needs to be fixed.
# sqr_rotate performs n rotations on d (clockwise: top -> rht, rht -> btm, btm -> left, left -> top)
def sqr_rotate(dct, n):
    print(f""" 
    ***********************************
    ***********************************
    BEFORE ROTATION:

            ---{dct['top']}----
            |      | 
            {dct['lft']}  1  {dct['rht']} 
            |      |
            ---{dct['btm']}---
     ***********************************
     ***********************************       
    """)
    res = deque(dct.values())
    res.rotate(n) # inline rotation on new data structure

    print(f""" 

    AFTER ROTATION:

            ---{dct['top']}----
            |      | 
            {dct['lft']}  1  {dct['rht']} 
            |      |
            ---{dct['btm']}---


    """)
    return dict(zip(dct.keys(), res))