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

from Crypto.Cipher import ARC2
from Crypto import Random
import base64

def ARC2_encrypt(msg,key):
    padding = " "
    block_size = ARC2.block_size
    p = lambda s:s + (block_size - len(s) % block_size) * padding
    iv = Random.new().read(8)
    c = ARC2.new(key,ARC2.MODE_CBC,iv)
    Enc_msg = iv + c.encrypt(p(msg).encode('ascii'))
    print("Your Encode >>> ",base64.b64encode(Enc_msg).decode('ascii'))
    print("-"*80)
    print("Your Key >>> ",key)
    print("-"*80)

def ARC2_decrypt(msg,key):
    iv = base64.b64decode(msg)[:8]
    Dec_msg = base64.b64decode(msg)[8:]
    d = ARC2.new(key,ARC2.MODE_CBC,iv)
    plain = d.decrypt(Dec_msg)
    print("Your Encode >>> ",plain.decode('ascii'))



print("""
[1] - To Encode ARC2
[2] - To Decode ARC2
[00] - Back
[0] - Exit
""")

x = int(input(">>>> "))
if x == 1 :
    y = input("Enter Your Plain Text : ")
    z = input("Enter Your Key : ")
    print("*"*80)
    ARC2_encrypt(y,z)
    print("*"*80)
elif x == 2 :
    y = input("Enter Your Encode Text : ")
    z = input("Enter Your Key : ")
    print("=="*40)
    ARC2_decrypt(y,z)
    print("=="*40)
elif x == 00 :
    import crypto
else :
    exit()
