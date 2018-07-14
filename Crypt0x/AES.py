# AES 256 encryption/decryption using pycrypto library

import sys
is_windows = sys.platform.startswith('win')

# Console Colors
if is_windows:
    # Windows deserves coloring too :D
    G = '\033[92m'  # green
    Y = '\033[93m'  # yellow
    B = '\033[94m'  # blue
    R = '\033[91m'  # red
    W = '\033[0m'   # white
    try:
        import win_unicode_console , colorama
        win_unicode_console.enable()
        colorama.init()
        #Now the unicode will work ^_^
    except:
        print("[!] Error: Coloring libraries not installed, no coloring will be used [Check the readme]")
        G = Y = B = R = W = G = Y = B = R = W = ''


else:
    G = '\033[92m'  # green
    Y = '\033[93m'  # yellow
    B = '\033[94m'  # blue
    R = '\033[91m'  # red
    W = '\033[0m'   # white


def banner():
    print("""%s
             #####                              ###   #     #
            #     # #####  #   # #####  #####  #   #   #   #
            #       #    #  # #  #    #   #   #     #   # #
            #       #    #   #   #    #   #   #     #    #
            #       #####    #   #####    #   #     #   # #
            #     # #   #    #   #        #    #   #   #   #
             #####  #    #   #   #        #     ###   #     #  %s%s
                # Coded By Mohamed Abdelfatah - X-Vector
                            fb/X.Vector1
    """ % (R, W, Y))


def parser_error(errmsg):
    banner()
    print("Usage: python " + sys.argv[0] + " [Options] use -h for help")
    print(R + "Error: " + errmsg + W)
    sys.exit()
banner()


import base64
from Crypto.Cipher import AES
from Crypto import Random
from Crypto.Protocol.KDF import PBKDF2





BLOCK_SIZE = int(input("Your Block Size Must Be (16 or 32) for AES \nEnter Your Block Size : "))
pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * chr(BLOCK_SIZE - len(s) % BLOCK_SIZE)
unpad = lambda s: s[:-ord(s[len(s) - 1:])]




def get_private_key(password):
    salt = b"this is a salt"
    kdf = PBKDF2(password, salt, 64, 1000)
    key = kdf[:32]
    return key


def encrypt(raw, password):
    private_key = get_private_key(password)
    raw = pad(raw)
    iv = Random.new().read(AES.block_size)
    cipher = AES.new(private_key, AES.MODE_CBC, iv)
    print("Your Encode >>> ",base64.b64encode(iv + cipher.encrypt(raw)).decode('ascii'))
    print("-"*80)
    print("Your Key >>> ",password)
    print("-"*80)



def decrypt(enc, password):
    private_key = get_private_key(password)
    enc = base64.b64decode(enc)
    iv = enc[:16]
    cipher = AES.new(private_key, AES.MODE_CBC, iv)
    print("Your Decode Text >>> ", unpad(cipher.decrypt(enc[16:])).decode('ascii'))


print("""
[1] - To Encode AES
[2] - To Decode AES
[00] - Back
[0] - Exit
""")

x = int(input(">>>> "))
if x == 1 :
    y = input("Enter Your Plain Text : ")
    z = input("Enter Your Key : ")
    print("*"*80)
    encrypt(y,z)
    print("*"*80)
elif x == 2 :
    y = input("Enter Your Encode Text : ")
    z = input("Enter Your Key : ")
    print("=="*40)
    decrypt(y,z)
    print("=="*40)
elif x == 00 :
    import crypto
else :
    exit()





# Let us decrypt using our original password
#decrypted = decrypt(encrypted, password)
#print(bytes.decode(decrypted))
