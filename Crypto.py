import random
def encrypt(plaintext, shift = random.randint(0, 10)):
    """Encrypt the plaintext using a Caesar cipher with the specified shift."""
    ciphertext = ''
    for char in plaintext:
        if char.isalpha():
            char_code = ord(char)
            char_code = (char_code - 65 + shift) % 26 + 65
            ciphertext += chr(char_code)
        else:
            ciphertext += char
    return ciphertext


def decrypt(ciphertext, shift):
    """Decrypt the ciphertext using a Caesar cipher with the specified shift."""
    plaintext = ''
    for char in ciphertext:
        if char.isalpha():
            # Shift the character back by the shift amount, wrapping around
            # the alphabet if necessary
            char_code = ord(char)
            char_code = (char_code - 65 - shift) % 26 + 65
            plaintext += chr(char_code)
        else:
            plaintext += char
    return plaintext
