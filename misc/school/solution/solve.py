from pwn import * 

def main():

    #change host
    HOST = "localhost"
    PORT = 8001

    p = remote(HOST, PORT)

    for i in range(3):

        p.recvuntil("expression: ")

        expression = p.recvline().rstrip().decode()
        solution = int(eval(expression))

        p.sendlineafter("answer: ", str(solution))

    
    flag = p.recv()
    print(flag)
    
if __name__ == "__main__":

    main()