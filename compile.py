string = " don\'t exist"
str_list = []
for i in string:
    str_list.append(ord(i))

print(f"str().join(map(chr,{str_list}))")

# a = [69, 110, 116, 101, 114, 32, 121, 111, 117, 114, 32, 80, 97, 115, 115, 119, 111, 114, 100, 32, 58, 32]
# print(''.join(map(chr,a)))