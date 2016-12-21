
# DAY 4 PART A:

# with open('inputday4.txt') as inp:
#     sum_code = 0
#     for line in inp:
#         letters = line[:-12]
#         checksum = line[-7:-2]
#         sect_ID = int(line[-11:-8])
#         # print letters, checksum, sect_ID
#         ldict = {}
#         for l in letters:
#             if l != '-':
#                 ldict[l] = ldict.get(l, 0) + 1
#         checksumtest = ''
#         sort_ldict = sorted(ldict.items(), key=lambda t: (-t[1], t[0]))
#         for i in range(5):
#             checksumtest += sort_ldict[i][0]
#         # print sort_ldict, checksum, checksumtest
#         if checksumtest == checksum:
#             print line, checksumtest, checksum, '\n'
#             sum_code += sect_ID

#     print sum_code

# dirs = ['aaaaa-bbb-z-y-x-123[abxyz]', 'a-b-c-d-e-f-g-h-987[abcde]', 'not-a-real-room-404[oarel]', 'totally-real-room-200[decoy]']

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

# DAY 4 PART B:

def get_real_letter(letter, sect_ID):

    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

    if letter == '-':
        return ' '

    i = sect_ID
    j = alphabet.index(letter)

    while i > 25:
        i -= 26

    index = i + j

    while index > 25:
        index -= 26


    return alphabet[index]


with open('inputday4.txt') as inp:

    for line in inp:
        letters = line[:-12]
        sect_ID = int(line[-11:-8])
        decrypt = ''

        for letter in letters:
            curr = get_real_letter(letter, sect_ID)
            decrypt += curr

        print decrypt, sect_ID

# direction = 'qzmt-zixmtkozy-ivhz-343[abxyz]'

# letters = direction[:-11]
# sect_ID = int(direction[-10:-7])
# decrypt = ''

# for letter in letters:
#     curr = get_real_letter(letter, sect_ID)
#     decrypt += curr

# print decrypt

