# CORES.PY

# Library with all the colors in python dictionaries
# made by me to make some things easier when writing terminal-printed code
# to use it effectively i recommend you to interpolate like this:
# print(f"{cores['YOUR COLOR']} YOUR TEXT {clear}")
# the clear at the end is necessary if you want the text colors/fx/bg to stop,
# so it doesn't extend to the rest of the code

clear = '\33[m'

cores = {
    'black': '\33[30m',
    'red': '\33[31m',
    'green': '\33[32m',
    'yellow': '\33[33m',
    'blue': '\33[34m',
    'purple': '\33[35m',
    'cyan': '\33[36m',
    'grey': '\33[37m',
    'white': '\33[97m',

# b at the start of the color name stands for brigther

    'darkgrey': '\33[90m',
    'bred': '\33[91m',
    'bgreen': '\33[92m',
    'byellow': '\33[93m',
    'bblue': '\33[94m',
    'bpurple': '\33[95m',
    'bcyan': '\33[96m',
}

bg = {
    'white': '\33[107m',
    'black': '\33[40m',
    'red': '\33[101m',
    'green': '\33[102m',
    'yellow': '\33[103m',
    'blue': '\33[104m',
    'purple': '\33[105m',
    'cyan': '\33[106m',
}

fx = {
    'normal': '\33[10m',
    'out': '\33[52m',
    'bold': '\33[1m',
    'italic': '\33[3m',
    'under': '\33[4m',
}
