# Overview
This is an exercise presented to me by realtor.com as part of the interview process. This text explains the problem and the steps I took to solve it.

# Problem
Write a program that accepts the name of a dictionary file as the single parameter. The dictionary file consists of a list of words and each word is on a separate line. <br />
The program should provide a command line prompt where the user can input a word of their choice. On hitting enter the program should find all anagrams in the provided dictionary file, if any exist, of the word and print them out on the next line as a comma separated list. If no anagrams are found it should print out “No anagrams found for _word_'”. The duration of each action should be measured and printed alongside the output.


### What is an Anagram?
An anagram is a word, phrase, or name formed by rearranging the letters of another, such as cinema, formed from iceman.

# Solution
## Assumptions
While solving the problem, I needed to make some assumptions about how to deal with cases that are not explained in the problem description. I would check them with my team at realtor.com if this was a real program. But since this is a coding challenge, I wrote the program with these assumptions:

- All non-alphabet letters (anyting other than a-z and A-Z) are ignored both in the dictionary and in the input word
- We do NOT try to remove duplicates in the dictionary. Duplicate anagrams are shown to the user if they exist.
- Anagrams are calculated case-insensitive

## Approach
Since we only consider alphabet letters (a-z and A-Z) and we ignore casing in finding anagrams, we can create a tuple with 26 numbers for each word showing the frequency of each lower-case letter starting at 'a' and ending at 'z'. <br />

For example, the word "access" has one 'a', two 'c's, one 'e', and two 's's. Therefore, the tuple is:<br />
(1, 0, 2, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0)<br />
Where each number shows the frequency of the following letters:<br />
(a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z)

The tuples are calculated for each word in the dictionary file and then stored in a python dictionary as key = tuple, value = all the words in the dictionary file that translate to this tuple.

After filling the python dictionary, the program prompts the user to enter words. For each word entered, the program calculates the tuple and tries to find it in the python dictionary. If the tuple exists in the python dictionary, it prints all the values (words with the same tuple). Otherwise, it prints a message that the word has no anagram in the dictionary.

## Complexity Analysis
### Time Complexity:
#### Initialization
O(NK), where N is the number of words and K is the average length of the words in the dictionary file.

#### Lookup
O(K) where K is the length of the word entered by the user.

### Space Complexity
O(NK), the total information content stored in the python dictionary

## Run Example
MacBookPro: ~$ python3 anagram_finder.py dictionary.txt

*Welcome to the Anagram Finder*<br />
*-----------------------------*<br />
*Initialized in 904.16 ms*

*AnagramFinder> stop*<br />
*4 anagrams found for stop in 0.04 ms*<br />
*post,spot,tops,stop*

*AnagramFinder> accept*<br />
*No anagrams found for accept in 0.03 ms*

*AnagramFinder> exit*<br />
*MacBookPro: ~$*

## Run Unit Tests
In order to run the unit tests, do:<br />

```MacBookPro: ~$ python3 unit_tests.py -b```

# Platform
This code is written with python 3.7
