import numpy as np
from Crypto.Util.strxor import strxor

CHARACTER_FREQ = {
    'a': 0.0651738, 'b': 0.0124248, 'c': 0.0217339, 'd': 0.0349835, 'e': 0.1041442, 'f': 0.0197881, 'g': 0.0158610,
    'h': 0.0492888, 'i': 0.0558094, 'j': 0.0009033, 'k': 0.0050529, 'l': 0.0331490, 'm': 0.0202124, 'n': 0.0564513,
    'o': 0.0596302, 'p': 0.0137645, 'q': 0.0008606, 'r': 0.0497563, 's': 0.0515760, 't': 0.0729357, 'u': 0.0225134,
    'v': 0.0082903, 'w': 0.0171272, 'x': 0.0013692, 'y': 0.0145984, 'z': 0.0007836, ' ': 0.1918182
}
def load_ciphertexts(file_path):
    with open(file_path, 'rb') as file:  # Open the file in binary read mode
        data = file.read()  # Read the entire content of the file as bytes
        # If ciphertexts are newline-separated in binary, you can split like this:
        chunk_size = 1000
        chunks = [data[i:i + chunk_size] for i in range(0, len(data), chunk_size)]
        return chunks # Split by newlines if they were used as delimiters

def analyze_keystream(ciphertexts, character_freq):
    max_len = max(len(c) for c in ciphertexts)
    keystream_guess = bytearray(max_len)
    for index in range(max_len):
        freqs = np.zeros(256)
        for byte_val in range(256):
            for c in ciphertexts:
                if index < len(c):
                    decrypted_char = chr(c[index] ^ byte_val)
                    if decrypted_char in character_freq:
                        freqs[byte_val] += character_freq.get(decrypted_char, 0)
        best_byte = np.argmax(freqs)
        keystream_guess[index] = best_byte
    return bytes(keystream_guess)

def decrypt_ciphertexts(ciphertexts, keystream):
    plaintexts = []
    for c in ciphertexts:
        extended_keystream = keystream[:len(c)]
        plaintext = strxor(c, extended_keystream)
        plaintexts.append(plaintext)
    return plaintexts

# Load ciphertexts from file
ciphertexts = load_ciphertexts('./longfile/file.enc')

# Perform frequency analysis to guess the keystream
keystream = analyze_keystream(ciphertexts, CHARACTER_FREQ)

# Decrypt the ciphertexts using the guessed keystream
plaintexts = decrypt_ciphertexts(ciphertexts, keystream)

# Print or save the decrypted plaintexts
for p in plaintexts:
    print(p.decode('utf-8', errors='replace'))
    #print(p.hex())

with open("./testo.txt", "w") as f:
    for p in plaintexts:
        f.write(p.hex())
