#!/usr/bin/env python
import sys
import words
from collections import deque

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
  if (len(argv) > 2):
    print "Usage: gridwords [--diagonal-on], defaulting to no diagonals"
  if (len(argv) == 2 and argv[1] == "--diagonal-on"):
    return True
  return False


def getGrid():
  return [
    ['a', 's', 'm', 'g', 'e'],
    ['f', 'e', 'o', 'n', 'l'],
    ['k', 't', 'h', 'i', 'd'],
    ['p', 'q', 'r', 'o', 'o'],
    ['u', 'v', 'w', 'x', 'y']]


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
  return lw



diagonals = parseArgs(sys.argv)
grid = getGrid()
graph = Graph(grid, diagonals)
longest_word = findLongestWordTraversal(graph)
print longest_word


