from collections import defaultdict
from typing import List
from file_exceptions import FileNotExpectedTypeError, IllegalArgumentError
import os
import sys


def find_anagrams(filepath: str) -> dict:
    """
    Opens a text file and finds anagrams by sorting each
    word alphabetically and using it as a key in a
    dictionary. Appends each word to the list corrensponding
    to the dictionary key.

    All keys are lowercase, thus finding the anagrams is not
    case-sensitive.

    :param filepath:str: the relative path to the current directory of the file to read from
    :raises:             FileNotFoundError if filename doesn't resolve to a relative path
    :rtype:              dictionary {sorted word: [words]}
    """
    anagrams = defaultdict(list)
    with open(filepath, 'r', encoding='utf-8') as file:
        for line in file:
            word = line.strip('\n')
            word_lower = word.lower()
            anagrams[''.join(sorted(word_lower))].append(word)
    return anagrams


def print_anagrams(anagrams: dict):
    """ 
    Prints all anagrams in the file

    :param anagrams:dict: Dictionary containing all possible anagrams
    """
    for anagram in anagrams.values():
        if len(anagram) > 1:
            print(', '.join(word for word in anagram))


def check_filetype(filename: str):
    """
    Checks if the file input is a .txt or .csv file to prevent the 
    user from uploading a wrong file.

    :param filename:str: Name of the file being checked
    :raises: FileNotExpectedTypeError if file is not .txt of .csv
    """
    if not filename.endswith('.txt') and not filename.endswith('.csv'):
        raise FileNotExpectedTypeError


def main(filepath: str = "eventyr.txt"):
    arguments = sys.argv

    if len(arguments) > 1:
        # Custom filepath has been given
        filepath = arguments[1]
    if len(arguments) > 2:
        raise IllegalArgumentError(
            "Only 2 arguments allowed: {script} and {filepath}")

    try:
        check_filetype(filepath)
        anagrams = find_anagrams(filepath)
        print_anagrams(anagrams)
    except FileNotExpectedTypeError:
        print('Please input a .txt or .csv file.')
    except FileNotFoundError:
        print('Could not find the file ', filepath)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()
