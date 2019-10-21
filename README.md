# Anagrams

## What is this?

`anagrams.py` is a program that inputs the path to a text or csv file containing one word for each line. It then finds all the one-worded anagrams within the file and prints them.

## Requirements

The only requirement to run this program is to have Python 3.5 or higher installed.

## How to run the program

Run the program by running the command

```console
$ python3 anagrams.py {filepath}
```

in the command line from the root folder, where `{filepath}` is an optional argument. `filepath` is the relative path to the file to read from. If no filepath is given, the program will use the default `eventyr.txt` file from the project folder.
