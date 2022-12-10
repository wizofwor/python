import argparse
import random


def main():
    #set parameters
    strength = 0.50 #strenght of the accent, number between 0 and 1

    #set parser
    parser = argparse.ArgumentParser(
        prog = 'l33t.py',
        description = "Converts text beetween clean text and b421c l33t",
        epilog = "example: l33t -t \"smack my hacker\" \n")
    parser.add_argument('-t', '--text',
        type=str, required=False, help='clean text to l33t')
    parser.add_argument('-l', '--l33t',
        type=str, required=False, help='l33t to clean text')
    args = parser.parse_args()

    #evaluate arguments
    if args.text:
        print(text_to_l33t(args.text, strength))
    elif args.l33t:
        print(l33t_to_text(args.l33t))
    else:
        print_help(parser)


def print_help(parser):
    print("ERROR: no input")
    parser.print_help()


def text_to_l33t(input, strength):
    """Take the clean text input and return leetspeak.
    input(string):        text to be converted
    strength(float, 0-1): how strong will be the conversion
    """
    charMap = {
    'a': ['4', '@'], 'c': ['(', '['], 'd': ['cl', ')'], 'e': ['3'],
    'f': ['ph'], 'h': ['#'], 'i': ['1', '!'], 'j': [']', ';'],
    'o': ['0'], 'p': ['9'], 'q': ['9'], 's': ['$', '5'],
    't': ['7', '+'], 'y': ['7'], 'z': ['2']}

    output = ''
    for char in input:
        if char.lower() in charMap and random.random() <= strength:
            alternatives = charMap[char.lower()]
            char = random.choice(alternatives)
        output = output + char
    return output


def l33t_to_text(input):
    """Take the basic l33t and return clean text."""
    charMap = {
    '4' : 'a', '@' : 'a', '(' : 'c', '[' : 'c',
    '3' : 'e', '#' : 'h', '1' : 'i', '!' : 'i',
    ']' : 'j', ';' : 'j', '0' : 'o', '9' : 'p',
    '$' : 's', '5' : 's', '7' : 'y', '2' : 'z'     }

    output = ""
    for char in input:
        if char in charMap:
            char = charMap[char]
        output = output + char
    return output


if __name__ == '__main__':
    main()
