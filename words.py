#!/usr/bin/env python
class AlphabetTree:
  """ A class for searching words and word prefixes """
  def __init__(self, value):
    self.endsWord = False
    self.value = value
    self.subtrees = []

  def insert(self, word):
    """ A method to insert the given word into this alphabet tree """
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
    """ Gives whether or not the given word is a valid word in this tree """
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
    """ Gives whether """
    if word == "":
      return True
    if word[0] in [t.value for t in self.subtrees]:
      for t in self.subtrees:
        if t.value == word[0]:
          return t.beginsValidWord(word[1:])
    else:
      return False

words = ""
with open('valid_words.txt', 'r') as f:
  words = f.readlines()
top = AlphabetTree('.')
for word in words:
  # each word ends with a \n so when inserting into the tree, we cut it off
  top.insert(word[:-1])
wordLookupTree = top


