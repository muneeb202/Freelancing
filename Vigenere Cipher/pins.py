def Vigenere_cipher(password, key):
    cypher = ""
    key_len = len(key)
    key_index = 0
    for char in password:
        if char.isalpha():
            shift = ord(key[key_index].upper()) - 65
            key_index += 1
            if key_index == key_len:
                key_index = 0
            shift_char = chr((ord(char.upper()) + shift - 65) % 26 + 65)
            if char.isupper():
                cypher += shift_char
            else:
                cypher += shift_char.lower()
        else:
            cypher += char
    return cypher

def Vigenere_decrypt(cypher, key):
    password = ""
    key_len = len(key)
    key_index = 0
    for char in cypher:
        if char.isalpha():
            shift = ord(key[key_index].upper()) - 65
            key_index += 1
            if key_index == key_len:
                key_index = 0
            shift_char = chr((ord(char.upper()) - shift - 65) % 26 + 65)
            if char.isupper():
                password += shift_char
            else:
                password += shift_char.lower()
        else:
            password += char
    return password


password = input("Enter the password: ")
key = input("Enter the key: ")


cypher = Vigenere_cipher(password, key)

print("The cypher is:", cypher)

password = Vigenere_decrypt(cypher, key)

print("The password is:", password)
