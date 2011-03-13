#!/c/python27/python

# Code for solving stages of The Python Challenge!!
# http://www.pythonchallenge.com/

import sys
import re
import os
import shutil
import commands
import string

# 1) http://www.pythonchallenge.com/pc/def/0.html
# Hint is big picture showing 2^38
def puzzle_1():
  return 2**38

  
  
def puzzle_2():
  # There a hint on the screen which suggests the translation table we make below, and a load of gibberish that we guess we should apply it to
  text = '''g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.'''
  table = string.maketrans('abcdefghijklmnopqrstuvwxyz','cdefghijklmnopqrstuvwxyzab')
  print "Applying mapping to gibberish:"
  print text.translate(table)
  print "Applying mapping to the url gives the following new url code:"
  return 'map'.translate(table)

def puzzle_3():
  return  
  
  
  
def main():
  args = sys.argv[1:]
  if not args:
    print "usage: n (n an integer - calls puzzle_n function";
    sys.exit(1)
    
  mappings = {1:puzzle_1,\
              2:puzzle_2,\
              3:puzzle_3}
  
  # Call the puzzle function given by commandline argument
  given_function = mappings[int(args[0])]
  print given_function()

  
    
    
    
    
    
if __name__ == "__main__":
  main()