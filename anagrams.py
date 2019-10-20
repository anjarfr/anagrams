from collections import defaultdict
from typing import List
import os


def find_anagrams(filename: str) -> dict:
    """
    Opens a text file and finds anagrams by sorting each
    word alphabetically. Appends each word to the list of
    the dictionary key that corresponds to the sorted word

    :param filename:str:    name of the file being opened.
                            Path is relative to current directory
    :raises:    FileNotFoundError if filename doesn't resolve to a
                relative path
    :rtype: dictionary of type {key=sorted word: value=[words]}
    """
    anagrams = defaultdict(list)
    with open(filename, 'r', encoding='utf-8') as file:
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


def main(filename: str):
    try:
        anagrams = find_anagrams(filename)
        print_anagrams(anagrams)
    except OSError as e:
        print('Could not find the file ', filename)
        print(e)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    main('eventyr.txt')
