def caesarCipher(text, shift):
    result = ""

    for i in text.upper():
        if i.isalpha():
            i = i.upper()
            shifted = chr((ord(i) - ord('A') + shift) % 26 + ord('A'))
            result += shifted
        else:
            result += i

    return result

def encrypt(text, shift):
    return caesarCipher(text, shift)

def decrypt(text, shift):
    return caesarCipher(text, -shift)

text = input("Enter message: ")

encrypted = encrypt(text, 13)
print("Encrypted:", encrypted)

decrypted = decrypt(encrypted, 13)
print("Decrypted:", decrypted)