
# dirs = ['aaaaa-bbb-z-y-x-123[abxyz]', 'a-b-c-d-e-f-g-h-987[abcde]', 'not-a-real-room-404[oarel]', 'totally-real-room-200[decoy]']

with open('inputday4.txt') as inp:
    sum_code = 0
    for line in inp:
        letters = line[:-12]
        checksum = line[-7:-2]
        sect_ID = int(line[-11:-8])
        # print letters, checksum, sect_ID
        ldict = {}
        for l in letters:
            if l != '-':
                ldict[l] = ldict.get(l, 0) + 1
        checksumtest = ''
        sort_ldict = sorted(ldict.items(), key=lambda t: (-t[1], t[0]))
        for i in range(5):
            checksumtest += sort_ldict[i][0]
        # print sort_ldict, checksum, checksumtest
        if checksumtest == checksum:
            print line, checksumtest, checksum, '\n'
            sum_code += sect_ID

    print sum_code

# sum_code = 0

# for d in dirs:
#     letters = d[:-11]
#     checksum = d[-6:-1]
#     sect_ID = int(d[-10:-7])
#     print letters, checksum, sect_ID
#     ldict = {}
#     for l in letters:
#         if l != '-':
#             ldict[l] = ldict.get(l, 0) + 1
#     checksumtest = ''
#     sort_ldict = sorted(ldict.items(), key=lambda t: (-t[1], t[0]))
#     for i in range(5):
#         checksumtest += sort_ldict[i][0]
#     print checksum, checksumtest
#     if checksumtest == checksum:
#         print checksum, checksumtest
#         sum_code += sect_ID

# print sum_code

    

