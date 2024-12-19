import string
import random
import sys
import secrets
from colorama import init, Style, Fore
import time
import os

init(autoreset=True)

print(Fore.CYAN + Style.BRIGHT + """
 PPPPP  AAAAA  SSSSS  SSSSS  W   W  OOO  RRRRR   DDDD   EEEEE  RRRRR
 P   P  A   A  S      S      W W W O   O R   R   D   D  E      R   R
 PPPPP  AAAAA  SSSSS  SSSSS  W W W O   O RRRRR   D   D  EEEE   RRRRR
 P      A   A      S      S  W W W O   O R  R    D   D  E      R  R
 P      A   A  SSSSS  SSSSS  W W W  OOO  R   R   DDDD   EEEEE  R   R
                                 
								-PASSWORDER
    """)

print(Fore.RED + Style.BRIGHT + "Password Generator - By Faijas")
print(Fore.YELLOW + "----------------------------------------------------")

# length input


def get_length():

    length = input(
        Fore.GREEN + "\nENTER THE LENGTH OF THE PASSWORD (MUST BE GREATER THAN 5): ")

    while True:

        if length.isdigit():
            length = int(length)

            # Check if the length is less than 6
            if length < 6:
                print(Fore.RED + "\nERROR: THE PASSWORD MUST BE GREATER THAN 5")

                length = input(Fore.GREEN + "\nENTER THE LENGTH AGAIN:")
            elif length > 128:
                print(
                    Fore.RED + "\nERROR: THE PASSWORD LENGTH MUST BE LESS THAN OR EQUAL TO 128")
                length = input(Fore.GREEN + "\nENTER THE LENGTH AGAIN:")
            else:
                return length
        else:
            # If the input is not a valid number, show an error
            print(Fore.RED + "\nERROR:\n")
            length = input(Fore.GREEN + "ENTER A VALID NUMBER:")


# main program


def pass_gen(length):

    char = string.ascii_lowercase + string.ascii_uppercase + \
        string.digits + string.punctuation

    password = [
        secrets.choice(string.ascii_lowercase),
        secrets.choice(string.ascii_uppercase),
        secrets.choice(string.digits),
        secrets.choice(string.punctuation),
    ]

    password += [secrets.choice(char) for _ in range(length-4)]

    secrets.SystemRandom().shuffle(password)

    return "".join(password)


while True:
    
    length = get_length()
    password = pass_gen(length)

    print("\n")

    # time delay

    for _ in range(3):
        for symbol in "-/\|":
            sys.stdout.write(
                Fore.BLUE + f"\rGENERATING YOUR PASSWORD {symbol}")
            sys.stdout.flush()
            time.sleep(0.1)

    sys.stdout.write("\r" + " " * 50 + "\r")

    # Print the generated password

    print(Fore.YELLOW + Style.BRIGHT + "\nYOUR PASSWORD IS: ", end="")
    print(Fore.WHITE + Style.BRIGHT + f"{password}")

    # Asking user for pass gen again

    again = input(Fore.GREEN +"\nDO YOU WANT TO GENERATE PASS AGAIN?Y/N:")
    
    while True:
        if again.lower() == "n":
            print("\n")
            for _ in range(3):
                for symbol in "-/\|":
                    sys.stdout.write(
                        Fore.BLUE + f"\rEXITING... {symbol} THANK YOU FOR USING PASSWORD GENARATOR  ")
                    sys.stdout.flush()
                    time.sleep(0.1)
                    
            os.system("cls" if sys.platform == "win32" else "clear")        
            break
        elif again.lower() == "y":
            break
        else:
            again = input(Fore.RED + "\nINVALID ENTRY ENTER Y/N:")
            
    if again == "n":
        break
    
        