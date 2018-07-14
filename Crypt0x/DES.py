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

from Crypto.Cipher import DES
from Crypto import Random
from Crypto.Util import Counter
import base64

def DES_encrypt(msg,key):
    block_size = DES.block_size # = 8
    iv = Random.new().read(int(DES.block_size/2))
    ctr = Counter.new(int(block_size*8/2) , prefix = iv)
    c = DES.new(key,DES.MODE_CTR,counter = ctr)
    encrypt_msg = iv + c.encrypt(msg.encode('ascii'))
    print("Your Encode >>> ",base64.b64encode(encrypt_msg).decode('ascii'))
    print("-"*80)
    print("Your Key >>> ",key)
    print("-"*80)
    # return[key,base64.b64encode(encrypt_msg).decode('ascii')]

def DES_decrypt(key,msg):
    block_size = DES.block_size # = 8
    iv = base64.b64decode(msg)[:4]
    Enc_msg = base64.b64decode(msg)[4:]
    ctr = Counter.new(int(block_size*8/2) , prefix = iv)
    d = DES.new(key,DES.MODE_CTR,counter = ctr)
    print("Your Decode Text >>> ", d.decrypt(Enc_msg).decode('ascii'))
    # return d.decrypt(Enc_msg).decode('ascii')



print("""
[1] - To Encode DES
[2] - To Decode DES
[00] - Back
[0] - Exit
""")

x = int(input(">>>> "))
if x == 1 :
    print("""
# Key size (must be 8 bytes long)
    """)
    y = input("Enter Your Plain Text : ")
    z = input("Enter Your Key : ")
    print("*"*80)
    DES_encrypt(y,z)
    print("*"*80)
elif x == 2 :
    y = input("Enter Your Encode Text : ")
    z = input("Enter Your Key : ")
    print("=="*40)
    DES_decrypt(z,y)
    print("=="*40)
elif x == 00 :
    import crypto
else :
    exit()
