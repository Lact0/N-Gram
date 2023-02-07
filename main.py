import csv, random
from ngram import *

chain, start = buildChain('Quotes/quoteData.txt')

quotes = []
with open('Quotes/quoteData.txt', 'r') as file:
  for row in file:
    quotes += [row.replace('\n', '')]

aiQuotes = []
with open('AI Quotes/aiQuotes.txt', 'r') as file:
  for row in file:
    aiQuotes += [row.replace('\n', '')]
    
#Functions

#Print and Save a new Bot-Generated Quote
def printQuote(n = 1):
  quotes = []
  for i in range(n):
    quote = ' '.join(generateLine(chain, start))
    quotes += [quote]
    print(quote)
  with open('AI Quotes/aiQuotes.txt', 'a') as file:
    for quote in quotes:
      file.write(quote)
      file.write('\n')

#Print the best Anime Quotes
def printFunny():
  with open('Quotes/good.txt', 'r') as file:
    for row in file:
      try:
        x = int(row) - 1
      except:
        continue
      print(quotes[x])
      print(' ')

#Print the best AI-generated Quotes
def printAiFunny():
  with open('AI Quotes/bestAiQuotes.txt', 'r') as file:
    for row in file:
      try:
        x = int(row) - 1
      except:
        continue
      print(aiQuotes[x])
      print(' ')