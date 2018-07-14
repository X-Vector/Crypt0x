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


from Crypto.Cipher import Blowfish
from Crypto import Random
import base64

def Blowfish_encrypt(msg,key):
    block_size = Blowfish.block_size
    iv = Random.new().read(Blowfish.block_size)
    padding = " "
    p = lambda s: s+(block_size - len(s) % block_size )*padding
    c = Blowfish.new(key,Blowfish.MODE_CBC,iv)
    encrypted = iv + c.encrypt(p(msg).encode('ascii'))
    print("Your Encode >>> ",base64.b64encode(encrypted).decode('ascii'))
    print("-"*80)
    print("Your Key >>> ",key)
    print("-"*80)


    #return [key , base64.b64encode(encrypted).decode('ascii')]

def Blowfish_decrypt(key , messege):
    block_size = Blowfish.block_size
    messege_ = base64.b64decode(messege)[8:]
    iv = base64.b64decode(messege)[:8]
    d = Blowfish.new(key,Blowfish.MODE_CBC,iv)
    print("Your Decode Text >>> ", d.decrypt(messege_).decode('ascii'))
    # return d.decrypt(messege_).decode('ascii')

print("""
[1] - To Encode Blowfish
[2] - To Decode Blowfish
[00] - Back
[0] - Exit
""")

x = int(input(">>>> "))
if x == 1 :
    y = input("Enter Your Plain Text : ")
    z = input("Enter Your Key : ")
    print("*"*80)
    Blowfish_encrypt(y,z)
    print("*"*80)
elif x == 2 :
    y = input("Enter Your Encode Text : ")
    z = input("Enter Your Key : ")
    print("=="*40)
    Blowfish_decrypt(z,y)
    print("=="*40)
elif x == 00 :
    import crypto
else :
    exit()
