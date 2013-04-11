#!/usr/bin/env python
import sys

class Twords():
  def __init__(self, dictionary = "words.txt"):
    self.dictionary = dictionary
  def match(self, word, rack):
    W = []
    r = list(rack)
    try:
      for w in list(word):
        W.append(r.pop(r.index(w)))
      return True
    except:
      return False
  def matches(self, rack):
    matches = []
    with open(self.dictionary) as f:
      for w in f.readlines():
        if self.match(w.rstrip(), rack):
          matches.append(w)
    return matches

def main():
  t = Twords()
  for match in t.matches(sys.argv[1]):
    print match.rstrip()

if __name__ == '__main__':
  main()
