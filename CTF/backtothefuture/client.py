# bit flipping against chacha with keystream reuse

import requests
import json
from Crypto.Cipher import ChaCha20
from Crypto.Random import get_random_bytes
from Crypto.Util.number import long_to_bytes, bytes_to_long
import time
# Define the URL of the server
url = "http://130.192.5.212:6522/"

s = requests.Session()

def sendData(newCookie, nonce):
    params = {
        "cookie": newCookie,
        "nonce": nonce
    }
    # Send the GET request
    response = s.get(url+"flag", params=params)
    # Check the response status code
    if response.status_code == 200:
        params = response.text
        print(params)
    else:
        print("Error")
        print(response.status_code)
        print(response.text)
        exit(1)



# Define the parameter
params = {
    "username": "michele",
    "admin": "1"
}
response = s.get(url+"login", params=params)
if response.status_code == 200:
    # Request was successful
    params = response.text
    print(params)

cookie = json.loads(params)["cookie"]
nonce = json.loads(params)["nonce"]

print(cookie)
firstCookie = long_to_bytes(cookie) # = encrypt("username=michele&expires={now + 30 days}&admin={admin}")
for i in range(10,266):
    tmpCookie = bytearray(firstCookie)
    now = int(time.time())+30*24*60*60 #now + 30
    sec = i*24*60*60 # i-day
    expire = now + sec
    expire = bytearray(str(expire).encode())
    now = bytearray(str(now).encode())
    for j in range(6):
        tmpCookie[25+j] = tmpCookie[25+j] ^ now[j]^expire[j] 

    print(str(tmpCookie.hex()))
    newCookie = bytes_to_long(tmpCookie)
    sendData(newCookie, nonce)

