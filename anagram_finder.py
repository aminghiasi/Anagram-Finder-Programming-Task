from collections import defaultdict
import re
import sys
import time
from functools import wraps


def timeit(my_func):
    """ A simple decorator that times the duration of a function's execution. """

    @wraps(my_func)
    def timed(*args, **kw):
        start_time = time.time()
        output = my_func(*args, **kw)
        finish_time = time.time()

        return output, (finish_time - start_time) * 1000

    return timed


class AnagramFinder:
    def __init__(self):
        self.dict = defaultdict(list)

    @timeit
    def read_dictionary(self, file_name: str):
        """ Given a file name, load it to memory as a dictionary. Each line in the file is considered a word.
        Also, words are case-sensitive and all non alphabetic letters are ignored. """

        try:
            with open(file_name) as infile:
                for word in infile:
                    if word == '' or word == '\n':
                        continue  # if there is an empty line, ignore it.

                    count = [0] * 26
                    stripped_word = re.sub('[^a-z]', '', word.lower())
                    if not stripped_word:
                        sys.exit(f'Fatal Error: word {word} in dictionary has no alphabet letters. Quitting...')

                    for char in stripped_word:
                        count[ord(char) - ord('a')] += 1
                    self.dict[tuple(count)].append(word.rstrip('\n'))

        except IOError:
            sys.exit(f'Fatal Error: Unable to open file {file_name}. Quitting...')

    @timeit
    def find_anagrams(self, word: str):
        """ Given a word, returns a list of it anagrams in the dictionary that has been already loaded to memory.
        None is returned if there is a problem in the input. """

        if not word:
            return None  # Return None if the input is empty

        stripped_word = re.sub('[^a-z]', '', word.lower())  # Remove anything that is not in alphabet
        if not stripped_word:
            print(f'{word} has no letter.')
            return None
        count = [0] * 26
        for char in stripped_word:
            count[ord(char) - ord('a')] += 1
        count_tuple = tuple(count)
        return [o for o in self.dict.get(count_tuple, []) if o != word]


def anagram_finder_main():
    """ The main function in anagram finder code. This function gets words as input in a terminal and finds the anagrams
     for each word in a previously provided dictionary. To quit, input 'exit'. """

    if len(sys.argv) != 2:
        sys.exit(f'Fatal Error: Expected only one argument. Found {len(sys.argv)-1}. Please enter the name'
                 f' of the dictionary file as argument. Quitting...')

    anagram_finder = AnagramFinder()

    _, initialization_time = anagram_finder.read_dictionary(sys.argv[1])
    print(f'Initialized in {initialization_time:.2f}ms')

    while 1 == 1:
        word = input("AnagramFinder> ")
        if word.lower() == 'exit':
            break
        anagrams, lookup_time = anagram_finder.find_anagrams(word)

        if anagrams is None:
            # if None is returned, it means that there was a problem in the input. Therefore, don't do anything
            continue

        if not anagrams:
            print(f'No anagrams found for {word} in {lookup_time:.2f}ms')
        else:
            print(f'{len(anagrams)} anagrams found for {word} in {lookup_time:.2f}ms')
            print(','.join(anagrams))


if __name__ == '__main__':
    anagram_finder_main()
