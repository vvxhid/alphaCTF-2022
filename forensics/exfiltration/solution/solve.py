
def main():

    with open("packets.txt", "r") as f:

        data = f.readlines()
        f.close()

    #remove new lines 
    for i in range(len(data)):

        data[i] = data[i].replace("\n", "").replace("\r", "")


    #remove empty elements 
    for item in data:

        if len(item) == 0:

            data.remove(item)

    #parsing the data and removing the additional '3'
    #before every char 
    png_bytes = []

    for item in data:

        if len(item) == 2:

            num = item[1]
            png_bytes.append(int(num))

        elif len(item) == 4:

            num = item[1] + item[3]
            png_bytes.append(int(num))

        elif len(item) == 6:

            num = item[1] + item[3] + item[5]
            png_bytes.append(int(num))
    
    png_bytes = bytearray(png_bytes)

    with open("flag.png", "wb") as f:

        f.write(png_bytes)
        f.close()


if __name__ == "__main__":

    main()