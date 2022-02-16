import pickle
import time
def iAmHere():
    data = b'\x80\x04\x95a\x00\x00\x00\x00\x00\x00\x00]\x94(KAK-K]K5KTK\x17KCK\x05K~KOK\x10KcKPKcK<KEKuK\x00K_K>KLK\x7fK KQK$K\x15K"K\x11KNK)K\x19K)KMK\x12KeKTKcK\x0bKTKaK\x0fKnK\x05K6K\x03K~e.'
    x = pickle.loads(data)
    n = ["A"]
    n.extend([chr(x) for x in [x[k]^x[k+1] for k in range(len(x)-1)]])

if __name__ == "__main__":
    print("Hi there")
    time.sleep(1)
    print("I hope you are doing well")
    time.sleep(1)
    print("I think you didn't undrestand the challenge")
    time.sleep(1)
    name = input("give your name: ")
    time.sleep(2)
    print(".", end="")
    time.sleep(1)
    print(".", end="")
    print(".", end="")
    time.sleep(1)
    print(".", end="")
    print(".", end="")
    print(".")
    time.sleep(1)
    print(f"so mr. {name}")
    time.sleep(1)
    print("I told you not to run me :))))))))))))")
    time.sleep(1)
    print("but you can check this youtube video, it may help you with this challenge: https://youtu.be/dQw4w9WgXcQ")
    time.sleep(1)
    print("have a nice day")