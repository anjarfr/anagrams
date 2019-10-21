from collections import defaultdict
from typing import List
from file_exceptions import FileNotExpectedTypeError
import os


def find_anagrams(filepath: str) -> dict:
    """
    Opens a text file and finds anagrams by sorting each
    word alphabetically. Appends each word to the list of
    the dictionary key that corresponds to the sorted word

    :param filepath:str: the relative path to the current directory of the file to read from
    :raises:             FileNotFoundError if filename doesn't resolve to a relative path
    :rtype:              dictionary {sorted word: [words]}
    """
    anagrams = defaultdict(list)
    with open(filepath, 'r', encoding='utf-8') as file:
        for line in file:
            word = line.strip('\n')
            anagrams[''.join(sorted(word))].append(word)
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
    Checks if the file input is a .txt or .csv file

    :param filename:str: Name of the file being checked
    :raises: FileNotExpectedTypeError if file is not .txt of .csv
    """
    if not filename.endswith('.txt') and not filename.endswith('.csv'):
        raise FileNotExpectedTypeError


def main(filepath: str):
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
    main('eventyr.txt')
