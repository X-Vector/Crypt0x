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
import hashlib
from cryptography.fernet import Fernet

def generate_b64_32byte_hash_from_string(string):
    byte_string = string.encode('utf-8')
    hasher = hashlib.sha256()
    hasher.update(byte_string)
    hash_32bytes = hasher.digest()
    b64_hash = base64.b64encode(hash_32bytes)
    return b64_hash

def get_fernet_encrypted_text(text_to_encrypt, encryption_key):
    b64_hash_key = generate_b64_32byte_hash_from_string(encryption_key)
    fernet_cipher = Fernet(b64_hash_key)
    bytes_to_encrypt = text_to_encrypt.encode("utf-8")
    encrypted_bytes = fernet_cipher.encrypt(bytes_to_encrypt)
    encrypted_text = encrypted_bytes.decode("utf-8")
    return [encrypted_text,encryption_key]

def get_fernet_decrypted_text(text_to_decrypt, encryption_key):
    b64_hash_key = generate_b64_32byte_hash_from_string(encryption_key)
    fernet_cipher = Fernet(b64_hash_key)
    bytes_to_decrypt = text_to_decrypt.encode('utf-8')
    decrypted_bytes = fernet_cipher.decrypt(bytes_to_decrypt)
    decrypted_text = decrypted_bytes.decode('utf-8')
    return decrypted_text



print("""
[1] - To Encode Fernet
[2] - To Decode Fernet
[00] - Back
[0] - Exit
""")

x = int(input(">>> "))
if x == 1:
    x = input("Your Plain text : ")
    y = input("Your Key : ")
    z = get_fernet_encrypted_text(x,y)
    print("-"*80)
    print("The Encrypted Messege >> ",z[0])
    print("-"*80)
    print("The Key >> ",z[1])
    print("-"*80)

elif x == 2:
    a = input("Your Encrypted text : ")
    b = input("Your Key : ")
    c = get_fernet_decrypted_text(a,b)
    print("Your Decode Text >>> ",c)
elif x == 00 :
    import crypto
else :
    exit()
