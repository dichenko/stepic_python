text = input()
shifr = input()

to_encode = input()
to_decode = input()

encode_dict = {}
decode_dict = {}


for i in range(len(text)):
    encode_dict[text[i]] = shifr[i]
    decode_dict[shifr[i]] = text[i]


to_encode_out = ''

for el in to_encode:
    to_encode_out += encode_dict[el]

to_decode_out = ''

for el in to_decode:
    to_decode_out += decode_dict[el]

print (to_encode_out)
print (to_decode_out)


