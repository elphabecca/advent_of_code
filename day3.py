def is_triangle(vals):

    for i, v in enumerate(vals):
        s = v
        vals[i] = 0
        if sum(vals) <= s:
            return False
        vals[i] = s

    return True

# def count_triangles():

#     inp = open('day3data.txt')
#     count = 0

#     for line in inp:
#         vals = [int(v) for v in line.strip().split()]

#         if is_triangle(vals):
#             count += 1

#     inp.close()
#     return count


# print count_triangles()

def count_triangles_b():

    inp = open('day3data.txt')
    num_lines = sum(1 for line in inp)
    inp.close()

    count = 0

    for i in range(0, num_lines, 3):
        with open('day3data.txt') as inp:
            each_three_lines = [[int(v) for v in item.strip().split()] for item in inp.readlines()[i:i+3]]
            print i, i+3, each_three_lines

            for i in range(3):
                sides = [each_three_lines[0][i], each_three_lines[1][i], each_three_lines[2][i]]
                print i, sides
                if is_triangle(sides):
                    count += 1

    return count


print count_triangles_b()




