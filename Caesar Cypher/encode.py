
def encode(key=4):
    string = input("Please enter the text to encode: ")
    encoded = ""

    for ch in string:
        num = ord(ch)
        num += key
        encoded += chr(num)

    print("Encoded text: " + encoded)

def decode(key=4):
    string = input("Please enter the text to decode: ")
    encoded = ""

    for ch in string:
        num = ord(ch)
        num -= key
        encoded += chr(num)

    print("Decoded text: " + encoded)

def main():

    while True:
        
        print("\n1) Encode text\n2) Decode text\n3) Exit program")
        opt = input("Please select an option (1-3): ")

        if opt == "1":
            encode()

        elif opt == "2":
            decode()

        elif opt == "3":
            break

        else:
            print("\nPlease select a valid option between 1 and 3.")

if __name__ == "__main__":
    main()