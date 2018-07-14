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

from Crypto.Cipher import ARC4
from Crypto.Hash import SHA
from Crypto import Random
import base64

def ARC4_encrypt(msg):
    key = Random.new().read(16)
    iv = Random.new().read(16)
    tempkey = SHA.new(iv+key).digest()
    c = ARC4.new(tempkey)
    print("Your Encode >>> ",base64.b64encode(c.encrypt(msg.encode('ascii'))))
    print("-"*80)
    print("Your Key >>> ",tempkey)
    print("-"*80)


    """
    print("Your Encode >>> ",base64.b64encode(c.encrypt(msg.encode('ascii'))))
    print("-"*80)
    print("Your Key >>> ",key)
    print("-"*80)"""

def ARC4_decrypt(msg,key):
    d = ARC4.new(key)
    print("Your Decode Text >>> ", d.decrypt(base64.b64decode(msg)))


print("""
[1] - To Encode ARC4
[2] - To Decode ARC4
[00] - Back
[0] - Exit
""")

x = int(input(">>>> "))
if x == 1 :
    y = input("Enter Your Plain Text : ")
    print("*"*80)
    ARC4_encrypt(y)
    print("*"*80)
elif x == 2 :
    y = input("Enter Your Encode Text : ")
    z = input("Enter Your Key : ")
    print("=="*40)
    ARC4_decrypt(y,z)
    print("=="*40)
elif x == 00 :
    import crypto
else :
    exit()
