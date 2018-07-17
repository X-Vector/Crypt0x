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

from Crypto.Cipher import DES3
from Crypto import Random
import base64

def DES3_encrypt(msg,key):
    block_size = DES3.block_size
    iv = Random.new().read(block_size)
    c = DES3.new(key,DES3.MODE_CBC,iv)
    messege = iv + c.encrypt(msg.encode('ascii'))
    print("The Encrypted Messege >> ",base64.b64encode(messege).decode('ascii'))
    print("-"*80)
    print("The Key >> ",key)
    print("-"*80)
    #return [key , base64.b64encode(messege).decode('ascii')]
def DES3_decrypt(key,messege):
    Encrypt_messege = base64.b64decode(messege)[8:]
    iv = base64.b64decode(messege)[:8]
    d = DES3.new(key,DES3.MODE_CBC,iv)
    print("Your Decode Text >>> ", d.decrypt(Encrypt_messege).decode('ascii'))
    # return d.decrypt(Encrypt_messege).decode('ascii')

print("""
[1] - To Encode DES3
[2] - To Decode DES3
[00] - Back
[0] - Exit
""")

def random_line(dir='keys.txt'):
    import random
    lines = open(dir).read().splitlines()
    myline = random.choice(lines)
    return myline


x = int(input(">>> "))
if x == 1:
    print("""
# Your Strings Must Be a Multiple of 8 in Length Like (8,16,24,...) char. Like (Mohammed , 12345678 , X-Vector)

# key size (must be either 16 or 24 bytes long)

    """)
     y = input("Enter Your Plain Text : ")
    z = input("Enter Your Key : ")
    anwser = str(input("Do You Want Generate a Random Key(y/n) : "))
    if anwser == 'y' or anwser = 'Y':
        z = random_line()
        print("Your Key Is : "+R+z+Y)
        print("Keep it Save")
    else:
        z = input("Enter Your Key : ")
    DES3_encrypt(y,z)

elif x == 2:
    c = input("Enter Your Encode Text : ")
    f = input("Enter Your Key : ")
    print(DES3_decrypt(f,c))
elif x == 00 :
    import crypto
else :
    exit()
