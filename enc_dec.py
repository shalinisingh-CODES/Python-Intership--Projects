diction = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def userInterface():

    fin = open("message.txt", "r")
    fout = open("cipher.txt", "w")

    container = fin.readlines()
    message = "".join(container)

    message = message.replace(" ", "")
    message = message.upper()

    user_input = input("Type 'e' for Encryption\nType 'd' for Decryption\n")

    if user_input == "e":
        print("Enter the key value")
        key = int(input())
        fout.write(Encrypt(message, key) + "\n")

    elif user_input == "d":
        print("Enter the key value")
        key = int(input())
        fout.write(Decrypt(message, key) + "\n")

    else:
        print("Wrong Input")
        userInterface()

    fin.close()
    fout.close()


def Encrypt(message, key):

    encrypted_message = ""

    for i in message:

        if i in diction:
            location = diction.index(i)
            location = location + key
            location = location % 26
            encrypted_message += diction[location]
        else:
            encrypted_message += i

    print("Encryption is done.\nPlease check cipher.txt")

    return encrypted_message


def Decrypt(message, key):

    decrypted_message = ""

    for i in message:

        if i in diction:
            location = diction.index(i)
            location = location - key
            location = location % 26
            decrypted_message += diction[location]
        else:
            decrypted_message += i

    print("Decryption is done.\nPlease check cipher.txt")

    return decrypted_message


userInterface()