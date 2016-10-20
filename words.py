#!/usr/bin/env python
class AlphabetTree:
  """ A class for searching words and word prefixes """
  def __init__(self, value):
    self.endsWord = False
    self.value = value
    self.subtrees = []

  def insert(self, word):
    if word == "":
      self.endsWord = True
      return
    if (word[0] in [t.value for t in self.subtrees]):
      for t in self.subtrees:
        if t.value == word[0]:
          t.insert(word[1:])
          return
    else:
      newNode = AlphabetTree(word[0])
      newNode.insert(word[1:])
      self.subtrees.append(newNode)

  def isValidWord(self, word):
    if word == "":
      if self.endsWord:
       return True
      else:
        return False
    if word[0] in [t.value for t in self.subtrees]:
      for t in self.subtrees:
        if t.value == word[0]:
          return t.isValidWord(word[1:])
    else:
      return False

  def beginsValidWord(self, word):
    if word == "":
      return True
    if word[0] in [t.value for t in self.subtrees]:
      for t in self.subtrees:
        if t.value == word[0]:
          return t.beginsValidWord(word[1:])
    else:
      return False

words_file_lines = ""
with open('words.csv', 'r') as f:
  words_file_lines = f.readlines()
words = [col[1][6:].lower() for col in [line.split(',') for line in words_file_lines]]
top = AlphabetTree('.')
for word in words:
  top.insert(word)
wordLookupTree = top


