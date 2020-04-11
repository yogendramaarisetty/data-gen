import colorama

colorama.init()
import sys
from termcolor import colored, cprint
import subprocess as sp
import translation_data



def chooseOption(number_of_options):
    try:
        cprint("Choose option from above", 'white', attrs=['bold'], end=": ")
        a = int(input())
        if a>0 and a<=number_of_options:
            return a
        else:
            cprint("Invalid Option", 'white', 'on_red')
            return chooseOption(number_of_options)
    except ValueError:
        cprint("Wrong Input! Please give integer input(option number)", 'white', 'on_red')
        print()
        return chooseOption(number_of_options)
    except KeyboardInterrupt:
        exit()


if __name__ == '__main__':
    cprint("DATA GENERATOR", 'green', attrs=['bold'])
    print(colored("OPTIONS\n [1] Translations lines\n", 'magenta'))
    translation_data.custom_trans_data()
