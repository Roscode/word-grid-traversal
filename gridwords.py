#!/usr/bin/env python
import sys
import words
from collections import deque
import string
import random as r

class Graph:
  """ An adjacency list implementation of graph """
  def __init__(self, grid, diagonals):
    self.vertices = []
    graphgrid = [0] * len(grid)
    for i in range(len(grid)):
      graphgrid[i] = [None] * len(grid[0])
    for i, row in enumerate(grid):
      for j, column in enumerate(row):
        node = Node(grid[i][j])
        self.vertices.append(node)
        graphgrid[i][j] = node
        if i > 0:
          Node.connectUndirected(graphgrid[i][j], graphgrid[i-1][j])
        if j > 0:
          Node.connectUndirected(graphgrid[i][j], graphgrid[i][j-1])
        if diagonals:
          if i > 0 and j > 0:
            Node.connectUndirected(graphgrid[i][j], graphgrid[i-1][j-1])
          if i > 0 and j < len(grid) - 1:
            Node.connectUndirected(graphgrid[i][j], graphgrid[i-1][j+1])



class Node:
  """ A node in a graph """
  def __init__(self, value):
    self.children = []
    self.value = value

  @staticmethod
  def connectUndirected(node_a, node_b):
    node_a.children.append(node_b)
    node_b.children.append(node_a)


def parseArgs(argv):
  diags = False
  rand = 0
  if (len(argv) > 4 or (len(argv) >= 2 and (argv[1] == '-h' or argv[1] == '--help'))):
    # e.g. ./gridwords.py --diagonal-on --random 6
    # produces a random 6x6 board
    # ./gridwords.py --random 4 produces random 4x4 board without diagonal traversal
    print("Usage: ./gridwords.py [--diagonal-on] [--random n]")
  if (len(argv) >= 2 and argv[1] == "--diagonal-on"):
    diags = True
  if (len(argv) >= 2):
    if (argv[1] == "--random"):
      rand = int(argv[2])
    if (len(argv) >= 3 and argv[2] == "--random"):
      rand = int(argv[3])
  return diags, rand



def getGrid(rand):
  """ Warning, does not check correct row length, so put the correct number of numbers in """
  if not rand:
    rows = eval(input("Enter the number of rows: "))
    result = []
    for i in range(rows):
      result.append(input("Enter row {0}: ".format(i + 1)).split())
    return result
  result = [[r.choice(string.ascii_lowercase) for i in range(rand)] for j in range(rand)]
  return result

#  return [
#    ['a', 's', 'm', 'g', 'e'],
#    ['f', 'e', 'o', 'n', 'l'],
#    ['k', 't', 'h', 'i', 'd'],
#    ['p', 'q', 'r', 'o', 'o'],
#    ['u', 'v', 'w', 'x', 'y']]


def findLongestWordTraversal(graph):
  lw = ""
  for v in graph.vertices:
    q = deque()
    q.appendleft((v, ""))
    while (len(q) > 0):
      current_vertex, wordSoFar = q.pop()
      current_word = wordSoFar + current_vertex.value
      if (not words.wordLookupTree.beginsValidWord(current_word)):
        continue
      if (words.wordLookupTree.isValidWord(wordSoFar + current_vertex.value) and len(lw) < len(current_word)):
        lw = current_word
      for child in current_vertex.children:
        q.appendleft((child, current_word))
      q.appendleft((current_vertex, current_word))
  return lw



diagonals, random = parseArgs(sys.argv)
grid = getGrid(random)
for i in grid:
  print(i)
graph = Graph(grid, diagonals)
longest_word = findLongestWordTraversal(graph)
print(longest_word)


