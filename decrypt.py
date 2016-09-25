import sys
import crypto

sys.modules['Crypto'] = crypto
from Crypto.Cipher import AES
from Crypto.Protocol.KDF import PBKDF2


# Function to get rid of padding
def clean(x):
    return x[:-x[-1]].decode('utf8')


# replace with your encrypted_value from sqlite3
encrypted_value = "(b'v107\xe2[\xb4\xbe\xcc\xfc\xcb0\xd5\xa3Ir\xb8\x9aG',"
print(len(encrypted_value))

# Trim off the 'v10' that Chrome/ium prepends
encrypted_value = encrypted_value[3:]
print(len(encrypted_value))

# Default values used by both Chrome and Chromium in OSX and Linux
salt = b'saltysalt'
iv = b' ' * 16
length = 16

# On Mac, replace MY_PASS with your password from Keychain
# On Linux, replace MY_PASS with 'peanuts'
my_pass = "Xx84862595$"
my_pass = my_pass.encode('utf8')

# 1003 on Mac, 1 on Linux
iterations = 1003

key = PBKDF2(my_pass, salt, length, iterations)
cipher = AES.new(key, AES.MODE_CBC, IV=iv)

decrypted = cipher.decrypt(encrypted_value)
print(clean(decrypted))
cookie = "_ga=GA1.2.579167751.1468206272;_lxsdk=15659ea99d1c8-0f531b4ec09c28-37667901-13c680-15659ea99d2c8;_lxsdk_s=7a066102ca5842b83d8c960f5cc1%7C;skmtutc=ReLDg9Ns+Vb5zelTllfYFyfqMVcnj5ZZMeIf93YLBtn7Ot/6OdGbSzJ17t9Wm8aRltEgEI6QDSeDD2wosNNkQw==-xElfA99KFYTWJRWYlw1XHKF+k/g=;TGC=5aebe8334e2040c3ba79*ee1ff8f9c7b;use_oldversion=2;JSESSIONID=0E635E74C325101A124D60A203B938AA"