#!/usr/bin/python

from __future__ import print_function
import sys, os, getopt, re
import nltk
from nltk.corpus import wordnet as wn

# Colors
red = '\x1b[31m'
green = '\x1b[32m'
yellow = '\x1b[33m'
blue = '\x1b[34m'
magenta = '\x1b[35m'
cyan = '\x1b[36m'
reset = '\x1b[0m'


def print_options(token, options):
    print()
    print(red + token + reset)
    print(red + '0)' + token + reset)
    for i, item in enumerate(options):
        print(green + '{}) {}'.format(i+1, item) + reset)


def get_choice(token):
    options = sorted(list(set(map(lambda x: x.name.split('.')[0], wn.synsets(token)))), reverse=True, key=lambda x: len(x))
    print_options(token, options)
    if(len(options) == 0):
        return token
    index = len(options) + 1
    while index > len(options):
        index = int(input('Chosen replacement => '))
    choice = options[index - 1] if index else token
    return choice

def get_files():
    input_file = ''
    output_file = ''
    args = sys.argv[1:]

    # Parse arguments
    try:
        opts, args = getopt.getopt(args, 'hi:o:', ['ifile=','ofile='])
    except getopt.GetoptError:
        print('Format should be \'smartify.py -i <input.txt> -o <output.txt>\'')
        sys.exit(1)
    for opt, arg in opts:
        if opt == 'h':
            print('Format should be \'smartify.py -i <input.txt> -o <output.txt>\'')
            sys.exit()
        elif opt in ('-i', '--ifile'):
            input_file = arg
        elif opt in ('-o', '--ofile'):
            output_file = arg
        else:
            print('invalid option: ' + opt)
            sys.exit(2)
    if not (input_file and output_file):
        print('Format should be \'smartify.py -i <input.txt> -o <output.txt>\'')
        sys.exit(3)
    else:
        return open(input_file, 'r'), open(output_file, 'w')


def smartify(infile, outfile):
    txt = infile.read()
    space_pattern = re.compile(r'\W+').finditer(txt)
    word_pattern = re.compile(r'\w+').finditer(txt)
    final_string = ''
    for word, space in zip(word_pattern, space_pattern):
        os.system('clear')
        print(final_string, end=' ')
        final_string += get_choice(word.group()) + space.group()
    os.system('clear')
    print(final_string)
    outfile.write(final_string)

if __name__ == "__main__":
    infile, outfile = get_files()
    smartify(infile, outfile)
