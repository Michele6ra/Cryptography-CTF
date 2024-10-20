import numpy
from string import *

CHARACTER_FREQ = {
    'a': 0.0651738, 'b': 0.0124248, 'c': 0.0207339, 'd': 0.0349835, 'e': 0.1041442, 'f': 0.0197881, 'g': 0.0158580,
    'h': 0.0492888, 'i': 0.0558094, 'j': 0.0009033, 'k': 0.0050529, 'l': 0.0331490, 'm': 0.0202024, 'n': 0.0564513,
    'o': 0.0596302, 'p': 0.0137645, 'q': 0.0008606, 'r': 0.0497563, 's': 0.0515760, 't': 0.0729357, 'u': 0.0225134,
    'v': 0.0082903, 'w': 0.0171272, 'x': 0.0013692, 'y': 0.0145984, 'z': 0.0007836, ' ': 0.1918182
} # ','
CHARACTER_FREQ111 = {
    'a': 0.0651738, 'b': 0.0124248, 'c': 0.7207339, 'd': 0.0349835, 'e': 0.1041442, 'f': 0.0197881, 'g': 0.0158580,
    'h': 0.0492888, 'i': 0.0558094, 'j': 0.0009033, 'k': 0.0050529, 'l': 0.0331490, 'm': 0.0202024, 'n': 0.0564513,
    'o': 0.7596302, 'p': 0.7137645, 'q': 0.0008606, 'r': 0.7497563, 's': 0.0515760, 't': 0.7729357, 'u': 0.0225134,
    'v': 0.0082903, 'w': 0.0171272, 'x': 0.0013692, 'y': 0.7145984, 'z': 0.0007836, ' ': 0.1918182, '{': 0.3000000,
    '}': 0.3000000, '-': 0.3000000, '1': 0.3000000, '2': 0.3000000, '3': 0.3000000, '4': 0.3000000, '5': 0.3000000,
    '6': 0.3000000, '7': 0.3000000, '8': 0.3000000, '9': 0.3000000, '0': 0.3000000,
} # ','
CHARACTER_FREQ1111 = {
    'c': 0.1000000, 'o': 0.1000000, 'p': 0.1000000, 'r': 0.1000000, 't': 0.1000000, 'y': 0.1000000, '{': 0.1000000,
    '2': 0.1000000, '4': 0.1000000, '}': 0.1000000,
}
#CRYPTO
# from CryptoPals S3C19/S3C20
# same key and same nonce: mount a keystream reuse attack
# encoded_ciphertexts = [b"SSBoYXZlIG1ldCB0aGVtIGF0IGNsb3NlIG9mIGRheQ==", b"Q29taW5nIHdpdGggdml2aWQgZmFjZXM=", b"RnJvbSBjb3VudGVyIG9yIGRlc2sgYW1vbmcgZ3JleQ==", b"RWlnaHRlZW50aC1jZW50dXJ5IGhvdXNlcy4=", b"SSBoYXZlIHBhc3NlZCB3aXRoIGEgbm9kIG9mIHRoZSBoZWFk", b"T3IgcG9saXRlIG1lYW5pbmdsZXNzIHdvcmRzLA==", b"T3IgaGF2ZSBsaW5nZXJlZCBhd2hpbGUgYW5kIHNhaWQ=", b"UG9saXRlIG1lYW5pbmdsZXNzIHdvcmRzLA==", b"QW5kIHRob3VnaHQgYmVmb3JlIEkgaGFkIGRvbmU=", b"T2YgYSBtb2NraW5nIHRhbGUgb3IgYSBnaWJl", b"VG8gcGxlYXNlIGEgY29tcGFuaW9u", b"QXJvdW5kIHRoZSBmaXJlIGF0IHRoZSBjbHViLA==", b"QmVpbmcgY2VydGFpbiB0aGF0IHRoZXkgYW5kIEk=", b"QnV0IGxpdmVkIHdoZXJlIG1vdGxleSBpcyB3b3JuOg==", b"QWxsIGNoYW5nZWQsIGNoYW5nZWQgdXR0ZXJseTo=", b"QSB0ZXJyaWJsZSBiZWF1dHkgaXMgYm9ybi4=", b"VGhhdCB3b20hbidzIGRheXMgd2VyZSBzcGVudA==", b"SW4gaWdub3JhbnQgZ29vZCB3aWxsLA==", b"SGVyIG5pZ2h0cyBpbiBhcmd1bWVudA==", b"VW50aWwgaGVyIHZvaWNlIGdyZXcgc2hyaWxsLg==", b"V2hhdCB2b2ljZSBtb3JlIHN3ZWV0IHRoYW4gaGVycw==", b"V2hlbiB5b3VuZyBhbmQgYmVhdXRpZnVsLA==", b"U2hlIHJvZGUgdG8gaGFycmllcnM/", b"VGhpcyBtYW4gaGFkIGtlcHQgYSBzY2hvb2w=", b"QW5kIHJvZGUgb3VyIHdpbmdlZCBob3JzZS4=", b"VGhpcyBvdGhlciBoaXMgaGVscGVyIGFuZCBmcmllbmQ=", b"V2FzIGNvbWluZyBpbnRvIGhpcyBmb3JjZTs=", b"SGUgbWlnaHQgaGF2ZSB3b24gZmFtZSBpbiB0aGUgZW5kLA==", b"U28gc2Vuc2l0aXZlIGhpcyBuYXR1cmUgc2VlbWVkLA==", b"U28gZGFyaW5nIGFuZCBzd2VldCBoaXMgdGhvdWdodC4=", b"VGhpcyBvdGhlciBtYW4gSSBoYWQgZHJlYW1lZA==", b"QSBkcnVua2VuLCB2YWluLWdsb3Jpb3VzIGxvdXQu", b"SGUgaGFkIGRvbmUgbW9zdCBiaXR0ZXIgd3Jvbmc=", b"VG8gc29tZSB3aG8gYXJlIG5lYXIgbXkgaGVhcnQs", b"WWV0IEkgbnVtYmVyIGhpbSBpbiB0aGUgc29uZzs=", b"SGUsIHRvbywgaGFzIHJlc2lnbmVkIGhpcyBwYXJ0", b"SW4gdGhlIGNhc3VhbCBjb20lZHk7", b"SGUsIHRvbywgaGFzIGJlZW4gY2hhbmdlZCBpbiBoaXMgdHVybiw=", b"VHJhbnNmb3JtZWQgdXR0ZXJseTo=", b"QSB0ZXJyaWJsZSBiZWF1dHkgaXMgYm9ybi4="]
encoded_ciphertexts = [b'734f9a37d0d03f8affe754bfa7dd17346a6a4ec4887cdf6ad682b1584cf0aeb105db5a507a3c63c2714e1748aa3c1a099c4e39e5a9374c7f938f3f9d3542e55b22e921082a', 
                       b'4542923184c06cc5f6b252f781a93375716117caf137df53df8cf40f56f1a7f54ad21c112e276390624b114efe2f1915d94e33f8a9265c73c088219a2601fa1e76f5261854d8', 
                       b'57468a2d9ede6cccffe006e88ce82534676a4c86c2729d5b9e83f85d57a2a1bd40d54c506732268b6002054aad2052139c5d22efa9215d3ac38e27922855e81270f4270a00d8', 
                       b'404b863084d622d9bcb247f180a9287b71255a8bca3edf4bcdc7d27d7ad2969a1780475e2e0363c2715a0247b13c1049920177c0e7270463dc896897204de15777ee6967', 
                       b'44559a2999d72dc6e3bc06c881a9346c6d764dcad13b8b56d192e50f50e9abbb05d7531c61262ac2634b0643b13b0147d24e23e8e62d4576da8831d86156e4036af23c1900d8', 
                       b'55429f2d97d023dfe3b244f685fa7f3a2a257884c2728651cbc7f24e4feee2a056945f0267396f8c754e0105fe171a129c4d22e8e527047bc793259d2201ef186fff3a4100d8', 
                       b'5e48866487d82bcfb0e547ed97a5716d6b701987d3209b5bcccbb1564cf7e2b64dd15d042274678c70021e42bb6e01089c5a24a1e82d403ac78e31d4354ead1a63f62c4d55a11dfb', 
                       b'45429f2d95cf298af9e601ecc4ef3e66246a4c98863d88509e81fd4e44aee2e214d659163c6464cf22444218f37a42068d026eb3ed26092b81992ec77913e94261ac7f432a']


print( [(encoded_ciphertexts[i].decode()) for i in range(len(encoded_ciphertexts))])
ciphertexts = [(bytes.fromhex(encoded_ciphertexts[i].decode())) for i in range(len(encoded_ciphertexts))]
print(ciphertexts)

print("stats")
print(len(ciphertexts))

longest_c = max(ciphertexts, key=len)
max_len = len(longest_c)
print(len(longest_c))

shortest_c = min(ciphertexts, key=len)
min_len = len(shortest_c)
print(len(shortest_c))

##################################################

candidates_list = []

for byte_to_guess in range(max_len):
    freqs = numpy.zeros(256, dtype=float)

    for guessed_byte in range(256):
        for c in ciphertexts:
            if byte_to_guess >= len(c):
                continue
            if chr(c[byte_to_guess] ^ guessed_byte) in printable:
                freqs[guessed_byte] += CHARACTER_FREQ.get(chr(c[byte_to_guess] ^ guessed_byte).lower(),0)

    max_matches = max(freqs)

    match_list = [(freqs[i], i) for i in range(256)]
    ordered_match_list = sorted(match_list, reverse=True)
    candidates_list.append(ordered_match_list)


keystream = bytearray()
for x in candidates_list:
    keystream += x[0][1].to_bytes(1,byteorder='big')
    

from Crypto.Util.strxor import strxor

keystream[28] = 89
keystream[20] = 119
keystream[3] = 125
keystream[38] = 105
keystream[40] = 97
keystream[17] = 115
keystream[34] = 123
keystream[42] = 115
keystream[58] = 109
keystream[59] = 105
keystream[60] = 99
keystream[65] = 98
keystream[53] = 100
keystream[49] = 97
keystream[67] = 116
keystream[69] = 115
keystream[43] = 99
keystream[45] = 114
keystream[46] = 111
#E-%c  s our CTF now... The world of the electr


dec28 = keystream[28] ^ ciphertexts[3][28]
dec20 = keystream[20] ^ ciphertexts[4][20]
dec3 = keystream[3] ^ ciphertexts[4][3]
dec38 = keystream[38] ^ ciphertexts[5][38]
dec40 = keystream[40] ^ ciphertexts[5][40]
dec17 = keystream[17] ^ ciphertexts[4][17]
dec34 = keystream[34] ^ ciphertexts[3][34]
dec42 = keystream[42] ^ ciphertexts[5][42]
dec65 = keystream[65] ^ ciphertexts[5][65]
dec58 = keystream[58] ^ ciphertexts[5][58]
dec59 = keystream[59] ^ ciphertexts[5][59]
dec60 = keystream[60] ^ ciphertexts[5][60]
dec53 = keystream[53] ^ ciphertexts[3][53]
dec49 = keystream[49] ^ ciphertexts[4][49]
dec67 = keystream[67] ^ ciphertexts[4][67]
dec69 = keystream[69] ^ ciphertexts[6][69]
dec43 = keystream[43] ^ ciphertexts[0][43]
dec45 = keystream[45] ^ ciphertexts[0][45]
dec46 = keystream[46] ^ ciphertexts[0][46]


mask28 = dec28 ^ ord('Y')
keystream[28] = keystream[28] ^ mask28
mask20 = dec20 ^ ord('w')
keystream[20] = keystream[20] ^ mask20
mask3 = dec3 ^ ord('}')
keystream[3] = keystream[3] ^ mask3
mask38 = dec38 ^ ord('i')
keystream[38] = keystream[38] ^ mask38
mask40 = dec40 ^ ord('a')
keystream[40] = keystream[40] ^ mask40
mask17 = dec17 ^ ord('s')
keystream[17] = keystream[17] ^ mask17
mask34 = dec34 ^ ord('{')
keystream[34] = keystream[34] ^ mask34
mask42 = dec42 ^ ord('s')
keystream[42] = keystream[42] ^ mask42
mask58 = dec58 ^ ord('m')
keystream[58] = keystream[58] ^ mask58
mask65 = dec65 ^ ord('b')
keystream[65] = keystream[65] ^ mask65
mask59 = dec59 ^ ord('i')
keystream[59] = keystream[59] ^ mask59
mask60 = dec60 ^ ord('c')
keystream[60] = keystream[60] ^ mask60
mask53 = dec53 ^ ord('d')
keystream[53] = keystream[53] ^ mask53
mask49 = dec49 ^ ord('a')
keystream[49] = keystream[49] ^ mask49
mask67 = dec67 ^ ord('t')
keystream[67] = keystream[67] ^ mask67
mask69 = dec69 ^ ord('s')
keystream[69] = keystream[69] ^ mask69
mask43 = dec43 ^ ord('c')
keystream[43] = keystream[43] ^ mask43
mask45 = dec45 ^ ord('r')
keystream[45] = keystream[45] ^ mask45
mask46 = dec46 ^ ord('o')
keystream[46] = keystream[46] ^ mask46




for c in ciphertexts:
    l = min(len(keystream),len(c))
    print(strxor(c[:l],keystream[:l]))
