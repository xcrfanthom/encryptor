def rsa_decrypt(ciphertext, private_key):
    return ''.join([chr(pow(int(char), private_key[0], private_key[1])) for char in ciphertext])

i = input("Enter a text to decrypt (comma-separated integers): ")
d = int(i.split(',')[0].strip())
n = int(i.split(',')[1].strip())
encrypted_message = list(map(int, (i.split(', '))[2:]))
private_key = (d, n)
decrypted_message = rsa_decrypt(encrypted_message, private_key)
print("Decrypted message:", decrypted_message)