import hashlib

text = 'ojvtpuvg'
# text = 'abc'
i = 0
decrypt = [0,0,0,0,0,0,0,0]
seen = set()

while len(seen) < 8:
    curr_test = text + str(i)
    curr_hash = hashlib.md5(curr_test)
    curr_hex = curr_hash.hexdigest()
    if i % 1000000 == 0:
        print i
    i += 1
    if curr_hex[:5] == '00000':
        print "*****\n", i, curr_hex, "\n*****"
        if curr_hex[5].isdigit():
            index = int(curr_hex[5])
            if index not in seen and index < 8:
                seen.add(index)
                decrypt[index] = curr_hex[6]
                print "*****\n", index, curr_hex[6], decrypt, "\n*****"

print ''.join(decrypt)
