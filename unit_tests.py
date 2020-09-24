import unittest
import anagram_finder


class TestAnagramFinder(unittest.TestCase):
    """Testing the AnagramFinder Class"""

    def test_long_word(self):
        anagrams, _ = self.anagram_finder_test.find_anagrams('kaleidoscopically')
        self.assertEqual(anagrams, [])

    def test_short_word(self):
        anagrams, _ = self.anagram_finder_test.find_anagrams('a')
        self.assertEqual(set(anagrams), {'A'})

    def setUp(self):
        self.anagram_finder_test = anagram_finder.AnagramFinder()
        self.anagram_finder_test.read_dictionary('dictionary.txt')

    def test_no_anagram(self):
        anagrams, _ = self.anagram_finder_test.find_anagrams('accept')
        self.assertEqual(anagrams, [])

    def test_stop(self):
        anagrams, _ = self.anagram_finder_test.find_anagrams('stop')
        self.assertEqual(set(anagrams), {'post', 'spot', 'tops'})

    def test_jean_pierre(self):
        anagrams, _ = self.anagram_finder_test.find_anagrams('Jean-Pierre')
        self.assertEqual(anagrams, [])

    def test_no_letter_in_word(self):
        anagrams, _ = self.anagram_finder_test.find_anagrams('123')
        self.assertEqual(anagrams, None)

    def test_no_input(self):
        anagrams, _ = self.anagram_finder_test.find_anagrams('')
        self.assertEqual(anagrams, None)




if __name__ == '__main__':
    unittest.main()