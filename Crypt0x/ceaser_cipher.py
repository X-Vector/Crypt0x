def rotated_letter(letter, key):
    if letter.isupper():
        start = ord('A')

    elif letter.islower():
        start = ord('a')

    else:
        return letter

    diff = ord(letter) - start
    position = (diff + key) % 26 + start

    return chr(position)

def rotated_string(string, key, encrypt=True):

    result = ""
    memo = {}

    if not encrypt:
        key = -key

    for character in string:
        if character in memo:
            # rot_cahr denotes rotated character
            rot_char = memo[character]
        else:
            rot_char = memo.setdefault(character, rotated_letter(character, key))

        result += rot_char


    return result


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


print("""
[1] - To Encode Ceaser Cipher
[2] - To Decode Ceaser Cipher
[00] - Back
[0] - Exit
""")

x = int(input(">>>> "))
if x == 1 :
    y = input("Enter Your Plain Text : ")
    z = int(input("Enter Your Key : "))
    print("*"*80)
    print("Your Encode >>> ",rotated_string(y,z))
    print("*"*80)
elif x == 2 :
    y = input("Enter Your Encode Text : ")
    z = int(input("Enter Your Key : "))
    print("=="*40)
    print("Your Plain Text >>> ",rotated_string(y, z , encrypt=False))
    print("=="*40)
elif x == 00 :
    import crypto
else :
    exit()
