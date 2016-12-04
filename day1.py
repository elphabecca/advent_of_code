directions = ['L5', 'R1', 'L5', 'L1', 'R5', 'R1', 'R1', 'L4', 'L1', 'L3', 'R2', 'R4', 'L4', 'L1', 'L1', 'R2', 'R4', 'R3', 'L1', 'R4', 'L4', 'L5', 'L4', 'R4', 'L5', 'R1', 'R5', 'L2', 'R1', 'R3', 'L2', 'L4', 'L4', 'R1', 'L192', 'R5', 'R1', 'R4', 'L5', 'L4', 'R5', 'L1', 'L1', 'R48', 'R5', 'R5', 'L2', 'R4', 'R4', 'R1', 'R3', 'L1', 'L4', 'L5', 'R1', 'L4', 'L2', 'L5', 'R5', 'L2', 'R74', 'R4', 'L1', 'R188', 'R5', 'L4', 'L2', 'R5', 'R2', 'L4', 'R4', 'R3', 'R3', 'R2', 'R1', 'L3', 'L2', 'L5', 'L5', 'L2', 'L1', 'R1', 'R5', 'R4', 'L3', 'R5', 'L1', 'L3', 'R4', 'L1', 'L3', 'L2', 'R1', 'R3', 'R2', 'R5', 'L3', 'L1', 'L1', 'R5', 'L4', 'L5', 'R5', 'R2', 'L5', 'R2', 'L1', 'L5', 'L3', 'L5', 'L5', 'L1', 'R1', 'L4', 'L3', 'L1', 'R2', 'R5', 'L1', 'L3', 'R4', 'R5', 'L4', 'L1', 'R5', 'L1', 'R5', 'R5', 'R5', 'R2', 'R1', 'R2', 'L5', 'L5', 'L5', 'R4', 'L5', 'L4', 'L4', 'R5', 'L2', 'R1', 'R5', 'L1', 'L5', 'R4', 'L3', 'R4', 'L2', 'R3', 'R3', 'R3', 'L2', 'L2', 'L2', 'L1', 'L4', 'R3', 'L4', 'L2', 'R2', 'R5', 'L1', 'R2']
test_dir = ['R8', 'R4', 'R4', 'R8']

cardinal = ['N', 'E', 'S', 'W']

def travel(dir_list):

    point_dir = cardinal[0]
    where_you_at = {'x' : 0,
                    'y' : 0}
    cartesian_dict = {'(0,0)' : 1}

    for direction in dir_list:
        point_dir = find_cardinal(direction, point_dir)
        units = int(direction[1:])

        axis = 'x'
        if point_dir in ['N','S']:
            axis = 'y'

        for unit in range(1, units+1):
            if axis == 'x':
                b = where_you_at['y']
                if point_dir == 'W':
                    a = where_you_at['x'] - unit
                if point_dir == 'E':
                    a = where_you_at['x'] + unit
                point = '(%s, %s)' % (a,b)
                cartesian_dict[point] = cartesian_dict.get(point, 0) + 1
                if cartesian_dict[point] == 2:
                    return point
            if axis == 'y':
                a = where_you_at['x']
                if point_dir == 'S':
                    b = where_you_at['y'] - unit
                if point_dir == 'N':
                    b = where_you_at['y'] + unit
                point = '(%s, %s)' % (a,b)
                cartesian_dict[point] = cartesian_dict.get(point, 0) + 1
                if cartesian_dict[point] == 2:
                    return point

        if point_dir in ['S', 'W']:
            units = -units
        where_you_at[axis] += units

    return cartesian_dict


def find_cardinal(instruction, curr_cardinal):

    curr_index = cardinal.index(curr_cardinal)

    if instruction[0] == 'L':
        if curr_index == 0:
            return cardinal[3]
        else:
            return cardinal[curr_index-1]

    if instruction[0] == 'R':
        if curr_index == 3:
            return cardinal[0]
        else:
            return cardinal[curr_index+1]


    # Part 1 Travel Code:

    # travel_dict = {'N' : 0,
    #                'E' : 0,
    #                'S' : 0,
    #                'W' : 0}

    # This was part of the for loop (after find_cardinal was called)
    # travel_dict[point_dir] += int(direction[1:])

    # x = travel_dict['E'] - travel_dict['W']
    # y = travel_dict['N'] - travel_dict['S']

    # shortest_distance = abs(x + y)

    # return shortest_distance

    # Part 2 Intersection:
    # This all went right after "point_dir = cardinal[0]"

    #     cartesian_dict = {'x' : 0,
    #                   'y' : 0}

    # def add_input(point_dir, units):
        
    #     cart = 'x'
    #     if point_dir in ['N','S']:
    #         cart = 'y'

    #     if point_dir in ['S', 'W']:
    #         units = -units

    #     cartesian_dict[cart] += units

    # Except for this line, which came after "units = int(direction[1:])":
    # add_input(point_dir, units)





