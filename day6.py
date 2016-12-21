def keywithmaxval(d):
     """ a) create a list of the dict's keys and values; 
         b) return the key with the max value"""  
     v=list(d.values())
     k=list(d.keys())
     return k[v.index(min(v))]

with open('day6inp.txt') as inp:
    col0 = {}
    col1 = {}
    col2 = {}
    col3 = {}
    col4 = {}
    col5 = {}
    col6 = {}
    col7 = {}
    for line in inp:
        line = line.strip()
        for i, char in enumerate(line):
            which_dict = 'col' + str(i)
            which_dict = eval(which_dict)
            which_dict[char] = which_dict.get(char, 0) + 1
    print keywithmaxval(col0)
    print keywithmaxval(col1)
    print keywithmaxval(col2)
    print keywithmaxval(col3)
    print keywithmaxval(col4)
    print keywithmaxval(col5)
    print keywithmaxval(col6)
    print keywithmaxval(col7)