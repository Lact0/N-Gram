import csv, random
from ngram import *

chain, start = buildChain('quoteData.txt')

quotes = []
with open('quoteData.txt', 'r') as file:
  for row in file:
    quotes += [row.replace('\n', '')]

aiQuotes = []
with open('aiQuotes.txt', 'r') as file:
  for row in file:
    aiQuotes += [row.replace('\n', '')]
    
#Functions
def printQuote():
  quote = ' '.join(generateLine(chain, start))
  print(quote)
  with open('aiQuotes.txt', 'a') as file:
    file.write(quote)
    file.write('\n')

def printFunny():
  with open('good.txt', 'r') as file:
    for row in file:
      try:
        x = int(row) - 1
      except:
        continue
      print(quotes[x])
      print(' ')

def printAiFunny():
  with open('bestAiQuotes.txt', 'r') as file:
    for row in file:
      try:
        x = int(row) - 1
      except:
        continue
      print(aiQuotes[x])
      print(' ')