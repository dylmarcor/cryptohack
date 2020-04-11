# Declare variables
binary = []
label = "label"

# Break label into binary and bitwise XOR with int 13
for s in list(label):
    # print(bin(ord(s ^ 13)))
    binary.append(bin(ord(s) ^ 13).lstrip('0b'))

# Convert the binary back to a string 
convert = "".join(chr(int(s, 2)) for s in  binary)
print(f'crypto{{{convert}}}')