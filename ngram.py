import csv, random
    
def buildChain(fileName):
  text = ''
  with open(fileName, 'r') as file:
    for line in file:
      line = clean(line)
      if line == '' or len(line) == 0:
        continue
      end = line[-1]
      if not (end == '.' or end == '?' or end == '!'):
        line += '.'
      text += ' ' + line
      
  text = text.lower().split()
  chain = {}
  start = {}
  beg = True
  
  for i in range(len(text) - 1):
    word = text[i]
    nextWord = text[i + 1]
    if word not in chain.keys():
      chain[word] = {}
    if nextWord not in chain[word].keys():
      chain[word][nextWord] = 0
    chain[word][nextWord] += 1
    if beg:
      if word not in start.keys():
        start[word] = 0
      start[word] += 1
      beg = False
    end = word[-1]
    if end == '.' or end == '?' or end == '!':
      beg = True
  
  for i in chain:
    total = 0
    for j in chain[i]:
      total += chain[i][j]
    for j in chain[i]:
      chain[i][j] /= total

  total = 0
  for i in start:
    total += start[i]
  for i in start:
    start[i] /= total
  
  return [chain, start]



def loadChain(fileName):
  file = open(fileName, 'r', encoding="utf8")
  chain = eval(file.readline())
  start = eval(file.readline())
  file.close()
  return (chain, start)
  
def generateLine(chain, start):
  ret = []
  gen = random.random()
  for i in start:
    gen -= start[i]
    if gen <= 0:
      ret += [i]
      break
  n = 0
  while ret[-1][-1] not in '.?!':
    word = ret[-1]
    gen = random.random()
    for i in chain[word]:
      gen -= chain[word][i]
      if gen <= 0:
        ret += [i]
        break
    if n > 100:
      break
  ret[0] = ret[0].capitalize()
  for i in range(len(ret)):
    if ret[i] == 'i':
      ret[i] = 'I'
  return ret


def clean(s):
  toClean = '[]"-`~+=/\\*'
  s = s.replace('\n', '')
  for i in toClean:
    s = s.replace(i, '')
  return s