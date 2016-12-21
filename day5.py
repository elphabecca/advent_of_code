import hashlib

text = 'ojvtpuvg'
# text = 'abc'
i = 0
decrypt = ''

while len(decrypt) < 8:
    curr_test = text + str(i)
    curr_hash = hashlib.md5(curr_test)
    curr_hex = curr_hash.hexdigest()
    if i % 10000000 == 0:
        print i
    i += 1
    if curr_hex[:5] == '00000':
        print "*****\n", i, curr_hex, "\n*****"
        decrypt += curr_hex[5]

print decrypt
