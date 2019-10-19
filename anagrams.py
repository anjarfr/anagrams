from collections import defaultdict
from typing import List
import os


def read_file(filename: str) -> List[str]:
    """
    Opens a text file and returns all the words in the
    file as a list

    :param filename:str: name of the file being opened. Path is relative to current directory
    :raises: 
    :rtype: 
    """
    with open(filename, 'r', encoding='utf-8') as file:
        words = file.read()
        word_array = words.split('\n')
    return word_array


def find_anagrams(word_list: List[str]) -> dict:
    """ 
    Finds anagrams by sorting each word alphabetically
    Appends each word to the list of the dictionary key
    that corresponds to the sorted word

    :param word_list:List[str]: list of words
    :raises: 
    :rtype: dictionary of type {key=sorted word: value=[words]}
    """
    anagrams = defaultdict(list)
    for word in word_list:
        anagrams[''.join(sorted(word))].append(word)
    return anagrams


def print_anagrams(anagrams: dict):
    """ 
    Prints all anagrams found in the list of words

    :param anagrams:dict: Dictionary containing all possible anagrams
    :raises:
    :rtype:
    """
    for anagram in anagrams.values():
        if len(anagram) > 1:
            print(', '.join(word for word in anagram))


def main():
    words = read_file('eventyr.txt')
    anagrams = find_anagrams(words)
    print_anagrams(anagrams)


if __name__ == '__main__':
    main()
