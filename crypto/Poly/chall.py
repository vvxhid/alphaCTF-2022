#!/usr/bin/python
from functools import reduce





def algorithm(value, key):
    result = (reduce(lambda x, y: x*value+y, key))
    return result%691


def main():
    with open("flag.txt", "r") as f:
        secret = [ord(x) for x in f.read().strip()]
    print('Welcome to the Avengers Cave of random items !')
    print('Prove yourself to the algorithm and the algorithm will reward you !!')
    while True:
        try:
            value = input("> ")
            if value == 'end':
                return
            value = int(value)
            enc = algorithm(value,secret)
            print(">> ", end="")
            print(enc)
        except ValueError:
            print("Invalid input. ")

if __name__ == '__main__':
    main()