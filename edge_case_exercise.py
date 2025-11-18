def move(my_list, direction):

    index_of_one = my_list.index(1)

    if direction == 'right' and index_of_one+1 == len(my_list):
        return my_list

    if direction == 'left' and index_of_one == 0:
        return my_list

    if direction == 'right':
        my_list[index_of_one] = 0
        my_list[index_of_one + 1] = 1

    if direction == 'left':
        my_list[index_of_one] = 0
        my_list[index_of_one - 1] = 1

    return my_list
