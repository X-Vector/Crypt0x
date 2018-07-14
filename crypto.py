import sys
import platform,os
clear = ""
if "Windows" in platform.system():
	clear = "cls"
if "Linux" in platform.system():
	clear = "clear"
os.system(clear)
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
a = print("""# Note : I'm Using MODE_CBC

[1] - AES
[2] - Ceaser Cipher
[3] - Blowfish
[4] - DES
[5] - DES3
[6] - ARC2
[7] - ARC4
[8] - Fernet
[9] - MultiFernet
[0] - To Exit
""")
x = int(input(">>> "))
if x == 1:
    os.system(clear)
    from Crypt0x import AES
elif x == 2:
    os.system(clear)
    from Crypt0x import ceaser_cipher
elif x == 3:
    os.system(clear)
    from Crypt0x import Blowfish
elif x == 4:
    os.system(clear)
    from Crypt0x import DES
elif x == 5:
    os.system(clear)
    from Crypt0x import DES3
elif x == 6:
    os.system(clear)
    from Crypt0x import ARC2
elif x == 7:
    os.system(clear)
    from Crypt0x import ARC4
elif x == 8:
    os.system(clear)
    from Crypt0x import Fernet
elif x == 9:
    os.system(clear)
    from Crypt0x import MultiFernet
else:
    exit()
