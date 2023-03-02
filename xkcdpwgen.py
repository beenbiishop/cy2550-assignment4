#!/usr/bin/env python3
import argparse
import random
import string

HELP_TEXT = """usage: xkcdpwgen [-h] [-w WORDS] [-c CAPS] [-n NUMBERS] [-s SYMBOLS]
                
Generate a secure, memorable password using the XKCD method
                
optional arguments:
    -h, --help            show this help message and exit
    -w WORDS, --words WORDS
                          include WORDS words in the password (default=4)
    -c CAPS, --caps CAPS  capitalize the first letter of CAPS random words
                          (default=0)
    -n NUMBERS, --numbers NUMBERS
                          insert NUMBERS random numbers in the password
                          (default=0)
    -s SYMBOLS, --symbols SYMBOLS
                          insert SYMBOLS random symbols in the password
                          (default=0)
"""


# Load word list from file
def load_word_list(word_list_path: str) -> list:
    with open(word_list_path, 'r') as f:
        return f.read().splitlines()


# Represents the password generator
class PasswordGenerator:
    def __init__(self, word_list_path: str):
        self.WORD_LIST = load_word_list(word_list_path)
        self.SYMBOL_LIST = string.punctuation
        self.NUM_LIST = [str(i) for i in range(10)]
        self.WORDS: [str] = []
        self.SYMBOLS: [str] = []
        self.NUMBERS: [str] = []

    # Generate the list of random words
    def __pick_words(self, num_words: int) -> None:
        # If the number of words is less than 1, return
        if num_words < 1:
            return
        # Pick a random sample of words from the word list and shuffle it
        self.WORDS = random.sample(self.WORD_LIST, num_words)
        random.shuffle(self.WORDS)

    # Generate the list of random symbols
    def __pick_symbols(self, num_symbols: int) -> None:
        # If the number of symbols is less than 1, return
        if num_symbols < 1:
            return
        # Pick a random sample of symbols from the symbol list and shuffle it
        self.SYMBOLS = random.sample(self.SYMBOL_LIST, num_symbols)
        random.shuffle(self.SYMBOLS)

    # Generate a list of random numbers
    def __pick_numbers(self, num_digits: int) -> None:
        # If the number of digits is less than 1, return
        if num_digits < 1:
            return
        # Pick a random sample of numbers from the number list and shuffle it
        self.NUMBERS = random.sample(self.NUM_LIST, num_digits)
        random.shuffle(self.NUMBERS)

    # Capitalize a random sample of words in the chosen word list
    def __capitalize_words(self, num_words: int) -> None:
        # If the number of words to capitalize is less than 1, return
        if num_words < 1:
            return
        for i in range(min(num_words, len(self.WORDS))):
            self.WORDS[i] = self.WORDS[i].capitalize()

    # Generate a password
    def generate_password(self, num_words: int = 4, num_caps: int = 0, num_symbols: int = 0,
                          num_digits: int = 0) -> str:
        # Generate the lists of words, symbols, and numbers based on the parameters
        self.__pick_words(num_words)
        self.__capitalize_words(num_caps)
        self.__pick_symbols(num_symbols)
        self.__pick_numbers(num_digits)

        # Combine the lists into a single list
        password_list = self.WORDS + self.SYMBOLS + self.NUMBERS

        # Shuffle the list
        random.shuffle(password_list)

        # Return the password as a string
        return ''.join(password_list)


# Parse command line arguments and generate a password
def main():
    parser = argparse.ArgumentParser(prog='XKCD Password Generator',
                                     description='Generate a secure password using the XKCD method.',
                                     add_help=False)
    parser.add_argument('-h', '--help', action='help', default=argparse.SUPPRESS, help=HELP_TEXT)
    parser.add_argument('-w', '--words', type=int, default=4, help='include WORDS words in the password (default=4)')
    parser.add_argument('-c', '--caps', type=int, default=0,
                        help='capitalize the first letter of CAPS random words (default=0)')
    parser.add_argument('-n', '--numbers', type=int, default=0,
                        help='insert NUMBERS random numbers in the password (default=0)')
    parser.add_argument('-s', '--symbols', type=int, default=0,
                        help='insert SYMBOLS random symbols in the password (default=0)')
    args = parser.parse_args()
    print(PasswordGenerator('words.txt').generate_password(args.words, args.caps, args.symbols, args.numbers))


# Execute main function
if __name__ == "__main__":
    main()
