#CST205 Lab14
#Nicholas Saunders

import os

def setMediaPathToCurrentDir():
  fullPathToFile = os.path.abspath(__file__)
  if fullPathToFile.startswith('/'):
    setMediaPath(os.path.dirname(fullPathToFile))
  else:
    setMediaPath(os.path.dirname(fullPathToFile) + '\\')

def problem1():
  setMediaPathToCurrentDir()
  maxValue = 0 
  numberOfWords = 0
  dict = {}
  fileName = open(getMediaPath() +"eggs.txt","r")
  for index in fileName:
    wordsList = index.split()
    numberOfWords += len(wordsList)
    index = index.lower()
    for word in index.split():
      try:
        dict[word] += 1
      except:
        dict[word] = 1
  for value1,value2 in dict.items():
    if value2 > maxValue:
      maxValue = value2
      maxKey = value1
  #outputs
  print "Total amount of words: ", numberOfWords
  print "Most commonly occuring word: ",maxKey,"appearing",maxValue,"times"
  print "List of words and their count: \n",dict
  fileName.close()
  
def problem2():
  setMediaPathToCurrentDir()
  infile = open(getMediaPath()+"press-releases.html","r")
  startStr = "uscb-margin-TB-02 uscb-title-3"
  line = ''
  ##formats best in full screen
  print " "*60 +"*"*10+"U.S. Census Bureau Headlines"+"*"*10
  for headline in infile:
    if startStr in line:
      print headline
    line = headline
  infile.close()