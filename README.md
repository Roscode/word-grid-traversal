Note: Written on python3 on this branch

A quick python solution for the problem of traversing a grid of letters to
find the longest word. Currently gets the list of valid words from a text file until I can find an api that will
give a huge list of words, so far I have only found apis that give definitions for specific
words.

To use, ./gridwords.py [--diagonal-on] [--random n].

The --diagonal-on flag is to decide whether a letter's neighbors includes the letters diagonal from that letter.

The --random flag creates a random nxn grid and uses that as input.
