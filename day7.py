with open('day7input.txt') as inp:
    count_true = 0
    for line in inp:
        line = line.strip()
        # print line
        in_brackets = False
        is_possible = False
        for i, char in enumerate(line):
            if i > 0 and i < len(line)-2:
                if char == '[':
                    in_brackets = True
                if char == ']':
                    in_brackets = False
                if char == line[i+1]:
                    # print char, line[i+1], i, "MAYBE"
                    if line[i-1] == line[i+2] and line[i-1] != char:
                        print "     ", i, line[i-1], char, line[i+1], line[i+2], in_brackets
                        if in_brackets:
                            print "          Nope, we're in brackets"
                            break
                        is_possible = True
            if i == len(line) - 1 and is_possible:
                print "          WE GOT A LIVE ONE"
                count_true += 1
                is_possible = False
    print count_true



