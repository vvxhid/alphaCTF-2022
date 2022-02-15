import pickle

flag = "AlphaCTF{1_s33_y0u_ar3_qu173_g00d_w17h_5nak35}"
print(flag)

## Exoring flag with itself

x = 0
new_flag = []
for i in flag:
    a = ord(i)
    x = x^a
    new_flag.append(x)
print(f"x is {x}")
print(new_flag)

## Remaking flag
final_flag = "A"
y = 0
for i in range(len(new_flag)-1):
    y = new_flag[i]
    a = new_flag[i+1]
    y = y^a
    final_flag+= chr(y)

print(final_flag)

print(pickle.dumps(new_flag))

print([chr(x) for x in [new_flag[k]^new_flag[k+1] for k in range(len(new_flag)-1)]])