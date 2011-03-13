#!/c/python27/python

# Code for solving stages of The Python Challenge!!
# http://www.pythonchallenge.com/

import sys
import re
import os
import shutil
import commands

# 1) http://www.pythonchallenge.com/pc/def/0.html
# Hint is big picture showing 2^38
def puzzle_1():
  return 2**38

  
  
def puzzle_2():
  return

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