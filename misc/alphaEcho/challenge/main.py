import os 

def main():

    print("Welcome to alphaEcho service")

    while True:

        option = input("Enter an order to alphaEcho ^^: ") 
        truncated_input = option[:3]

        if "sh" in truncated_input:
            print("Nope !")
            
        else:

            try:

                print("Output of alphaEcho " + truncated_input + ":")
                print(os.system("echo" + truncated_input))

            except:

                print("Something is wrong :/")


if __name__ == "__main__":

    main()