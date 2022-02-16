X = 1337
with open('./flag.txt', 'r') as file:
    flag = file.read().rstrip()

flag_bytes = [ord(x)^X for x in flag]
print(flag_bytes)
print([chr(x^X) for x in flag_bytes])