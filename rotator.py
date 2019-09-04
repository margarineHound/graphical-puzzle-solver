from collections import deque

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

def check(square):
    rotate_n = 0
    new_list=[]
    for item in square:
        if item['top'] is 'b':
            rotate_n = 1
        if item['top'] is 'c':
            rotate_n = 2
        if item['top'] is 'd':
            rotate_n = 3
        if rotate_n != 0:    
            new_list.append(sqr_rotate(item, rotate_n))
        else:
            new_list = square

    return new_list
    
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

            ---{new_dict_values[1]}----
            |      | 
            {new_dict_values[0]}  1  {new_dict_values[2]} 
            |      |
            ---{new_dict_values[3]}---


    """)
    return dict(zip(dict1.keys(), new_dict_values))

   
def main():
    delt = [{'lft': 'a', 'top': 'b', 'rht': 'c', 'btm': 'd'}, {'lft': 'd', 'top': 'a', 'rht': 'c', 'btm': 'b'} ,{'lft': 'a', 'top': 'b', 'rht': 'c', 'btm': 'd'}, {'lft': 'b', 'top': 'c', 'rht': 'd', 'btm': 'a'} ,{'lft': 'c', 'top': 'd', 'rht': 'a', 'btm': 'b'}, {'lft': 'd', 'top': 'a', 'rht': 'b', 'btm': 'c'},{'lft': 'a', 'top': 'b', 'rht': 'c', 'btm': 'd'}, {'lft': 'b', 'top': 'c', 'rht': 'd', 'btm': 'a'},{'lft': 'c', 'top': 'd', 'rht': 'a', 'btm': 'b'} ] 
    verify(delt)
    rot = check(delt)
    print(f"""    

    ***************************************************
    **                  FINAL VERSION               **
    ***************************************************

    ---{rot[0]['top']}------{rot[1]['top']}-------{rot[2]['top']}--
    |      |       |      |
    {rot[0]['lft']}  1  {rot[0]['rht']}/{rot[1]['lft']}  2  {rot[1]['rht']}/{rot[2]['lft']}  3  {rot[2]['rht']} 
    |      |       |      |
    |--{rot[0]['btm']}/{rot[3]['top']}----{rot[1]['btm']}/{rot[4]['top']}----{rot[2]['btm']}/{rot[5]['top']}--|
    |      |       |      |
    {rot[3]['lft']}  4  {rot[3]['rht']}/{rot[4]['lft']}  5  {rot[4]['rht']}/{rot[5]['lft']}  6  {rot[5]['rht']} 
    |      |       |      |
    |--{rot[3]['btm']}/{rot[6]['top']}----{rot[4]['btm']}/{rot[7]['top']}----{rot[5]['btm']}/{rot[8]['top']}--|
    |      |       |      |
    {rot[6]['lft']}  7  {rot[6]['rht']}/{rot[7]['lft']}  8  {rot[7]['rht']}/{rot[8]['lft']}  9  {rot[8]['rht']} 
    |      |       |      |
    |--{rot[6]['btm']}------{rot[7]['btm']}--------{rot[8]['btm']}--|

    """)
if __name__ == "__main__": main()
