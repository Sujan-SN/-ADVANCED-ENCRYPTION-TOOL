
from Cryptodome.Cipher import AES
from Cryptodome.Util.Padding import unpad

# Load key and salt from file
with open('key.bin', 'rb') as f:
    salt = f.read(32)
    key = f.read()

# Load encrypted data from file
with open('encrypted_data.bin', 'rb') as f:
    iv = f.read(16)
    decrypted_data = f.read()

# Decrypt data
cipher = AES.new(key, AES.MODE_CBC, iv=iv)
original = unpad(cipher.decrypt(decrypted_data), AES.block_size)

print("Decrypted Data:", original.decode())

# Save decrypted data to file
with open('decrypted_data.txt', 'w') as f:
    f.write(original.decode())

      