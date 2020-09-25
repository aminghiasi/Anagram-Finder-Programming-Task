from collections import defaultdict
import re
import sys
import time
from functools import wraps


def timeit(func: callable) -> tuple:
    """ A simple decorator that times the duration of a function's execution. """

    @wraps(func)
    def timed(*args, **kw):
        start_time = time.time()
        output = func(*args, **kw)
        finish_time = time.time()

        return output, (finish_time - start_time) * 1000

    return timed


class AnagramFinder:
    """This class contains the data structure and methods to find the anagrams of a given word in a dictionary file."""

    def __init__(self):
        self.dict = defaultdict(list)

    @staticmethod
    def calculate_frequency_tuple(word: str) -> tuple:
        """ For a given word, this method calculates the frequency tuple. A frequency tuple is a tuple with 26
        integers showing the frequency of each english letter from 'a' to 'z'"""

        count = [0] * 26
        for char in word:
            count[ord(char) - ord('a')] += 1

        return tuple(count)

    @timeit
    def read_dictionary(self, file_name: str) -> None:
        """ Given a dictionary file, load it to memory as a python dictionary for anagram lookup.
        Each line in the file is considered a word. Also, words are case-insensitive and all
        non alphabetic letters are ignored. """

        try:
            with open(file_name, 'r') as infile:
                for word in infile:
                    if word == '' or word == '\n':
                        continue  # if there is an empty line, ignore it.

                    # remove non-alphabet characters and convert all letters to lower case
                    stripped_word = re.sub('[^a-z]', '', word.lower())
                    if not stripped_word:
                        sys.exit(f'Fatal Error: word {word} in dictionary has no alphabet letters. Quitting...')

                    # translate the stripped word into a frequency tuple and store it in the dictionary
                    self.dict[AnagramFinder.calculate_frequency_tuple(stripped_word)].append(word.rstrip('\n'))

        except IOError:
            sys.exit(f'Fatal Error: Unable to open file {file_name}. Quitting...')

    @timeit
    def find_anagrams(self, word: str) -> list:
        """ Given a word, returns a list of its anagrams in the dictionary that has been already loaded to memory.
        None is returned if there is a problem in the input. """

        if not word:
            return None  # Return None if the input is empty

        # remove non-alphabet characters and convert all letters to lower case
        stripped_word = re.sub('[^a-z]', '', word.lower())

        if not stripped_word:
            print(f'{word} has no letter.')
            return None

        # translate the stripped word into the frequency tuple and try to find it in the dictionary
        return self.dict.get(AnagramFinder.calculate_frequency_tuple(stripped_word), [])


def anagram_finder_main() -> None:
    """ The main function in anagram finder code. This function gets words as input in a terminal and finds the anagrams
    for each word in a previously provided dictionary. To quit, input 'exit'. """

    if len(sys.argv) != 2:
        sys.exit(f'Fatal Error: Expected only one argument. Found {len(sys.argv)-1}. Please enter the name'
                 f' of the dictionary file as argument. Quitting...')

    anagram_finder = AnagramFinder()

    _, initialization_time = anagram_finder.read_dictionary(sys.argv[1])

    print('\nWelcome to the Anagram Finder')
    print('-----------------------------')
    print(f'Initialized in {initialization_time:.3f} ms\n')

    while 1 == 1:
        word = input("AnagramFinder> ")
        if word.lower() == 'exit':
            break
        anagrams, lookup_time = anagram_finder.find_anagrams(word)

        if anagrams is None:
            # if None is returned, it means that there was a problem in the input. Therefore, don't do anything
            continue

        if not anagrams:
            print(f'No anagrams found for {word} in {lookup_time:.3f} ms')
        else:
            print(f'{len(anagrams)} anagrams found for {word} in {lookup_time:.3f} ms')
            print(','.join(anagrams))
        print()


if __name__ == '__main__':
    anagram_finder_main()
