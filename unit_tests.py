import unittest
import anagram_finder


class TestAnagramFinder(unittest.TestCase):
    """Testing the AnagramFinder Class"""

    def setUp(self):
        file_name = 'dictionary_unit_test.txt'
        words_to_write = ['kaleidoscopically', 'aaccdeiikllloopsy', 'oh', 'ho', 'stop', 'pots', 'opts', 'tops', 'spot',
                          'post', 'Jean-Pierre', 'PierreJean']
        try:
            with open(file_name, 'w') as outfile:
                for word in words_to_write:
                    outfile.write(word+'\n')

        except IOError:
            sys.exit(f'Fatal Error: Unable to create/change file {file_name}. Quitting...')

        self.anagram_finder_test = anagram_finder.AnagramFinder()
        self.anagram_finder_test.read_dictionary(file_name)

    def test_long_word(self):
        anagrams, _ = self.anagram_finder_test.find_anagrams('kaleidoscopically')
        self.assertEqual(set(anagrams), {'aaccdeiikllloopsy', 'kaleidoscopically'})

    def test_short_word(self):
        anagrams, _ = self.anagram_finder_test.find_anagrams('oh')
        self.assertEqual(set(anagrams), {'oh', 'ho'})

    def test_no_anagram(self):
        anagrams, _ = self.anagram_finder_test.find_anagrams('accept')
        self.assertEqual(anagrams, [])

    def test_many_anagrams(self):
        anagrams, _ = self.anagram_finder_test.find_anagrams('stop')
        self.assertEqual(set(anagrams), {'post', 'spot', 'tops', 'stop', 'opts', 'pots'})

    def test_with_dash(self):
        anagrams, _ = self.anagram_finder_test.find_anagrams('Jean-Pierre')
        self.assertEqual(set(anagrams), {'Jean-Pierre', 'PierreJean'})

    def test_with_non_alphabet_letters(self):
        anagrams, _ = self.anagram_finder_test.find_anagrams('Jean-Pierre123%^&`')
        self.assertEqual(set(anagrams), {'Jean-Pierre', 'PierreJean'})

    def test_no_letter_in_word(self):
        anagrams, _ = self.anagram_finder_test.find_anagrams('123~$8')
        self.assertEqual(anagrams, None)

    def test_no_input(self):
        anagrams, _ = self.anagram_finder_test.find_anagrams('')
        self.assertEqual(anagrams, None)


if __name__ == '__main__':
    unittest.main()