def encrypt_substitution(message, key):
    polynomial = "x^128+x^95+x^57+x^45+x^38+x^36+1"
    encrypted_message = ""
    for char in message.lower():
        if char in polynomial:
            index = polynomial.index(char)
            encrypted_char = polynomial[(index + key) % 26]
            encrypted_message += encrypted_char
        else:
            encrypted_message += char
    return encrypted_message

def decrypt_substitution(encrypted_message, key):
    return encrypt_substitution(encrypted_message, -key)

original_message = "000000000000000000000000000000000100000000000000000000000000000000000001000000000001000000101000000000000000000000000000000000001"
key = 2
encrypted = encrypt_substitution(original_message, key)
decrypted = decrypt_substitution(encrypted, key)

print(f"Original message: {original_message}")
print(f"Encrypted message: {encrypted}")
print(f"Decrypted message: {decrypted}")
