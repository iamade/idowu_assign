from Crypto.PublicKey import RSA

# Generate a public-private key pair
key = RSA.generate(key_size=256)

# Extract the public and private keys
public_key = key.publickey()
private_key = key
