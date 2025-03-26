from Cryptodome.Random import get_random_bytes
from Cryptodome.Protocol.KDF import PBKDF2
from Cryptodome.Cipher import AES
from Cryptodome.Util.Padding import pad

# Generate a random salt
salt = get_random_bytes(32)

# Password and key derivation
password = "mypassword"
key = PBKDF2(password, salt, dkLen=32)

# Message encryption
message = b"Hi, I am an Intern at CodeTech"
cipher = AES.new(key, AES.MODE_CBC)
ciphered_data = cipher.encrypt(pad(message, AES.block_size))

# Save encrypted data to file
with open('encrypted_data.bin', 'wb') as f:
    f.write(cipher.iv)
    f.write(ciphered_data)

# Save key and salt to file
with open('key.bin', 'wb') as f:
    f.write(salt)
    f.write(key)

print("Encrypted Data:", ciphered_data.hex())


