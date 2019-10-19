def read_file(filename):
    with open(filename, 'r') as file:
        word_array = file.readlines()
    return word_array


def main():
    words = read_file('eventyr.txt')


if __name__ == '__main__':
    main()
