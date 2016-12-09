def is_triangle(vals):

    for i, v in enumerate(vals):
        s = v
        vals[i] = 0
        if sum(vals) <= s:
            return False
        vals[i] = s

    return True

def count_triangles():

    inp = open('day3data.txt')
    count = 0

    for line in inp:
        vals = [int(v) for v in line.strip().split()]

        if is_triangle(vals):
            count += 1
            print vals

    inp.close()
    return count


print count_triangles()

