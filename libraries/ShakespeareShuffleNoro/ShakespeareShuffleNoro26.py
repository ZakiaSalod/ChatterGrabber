from sys import path
from os import getcwd

parent = '/'.join(getcwd().split('/')[:])

if parent not in path:
	path.insert(0, parent)
import optimizeClassifier

files = ['NLTK_Ready_Tweets.csv']
cores = 1
iterations = 1
sweepRange = [0.9]
degrees =  []
SVMMode = 'number'
SVMNumber = 1000
NLPFreqLimit = []
stops = 0
prefix = ''



fileName = "ShakespeareShuffleNoro/ShakespeareShuffleNoro26Score.txt"
index = 26
gen = 5

SVMMode = 'number'
degrees.append(3)
SVMMode = 'number'
degrees.append(6)
SVMMode = 'number'
mode = ["decision tree"]
NLPFreqLimit.append(1)
mode = ["decision tree"]
mode = ["naive bayes"]
mode = ["max ent"]
degrees.append(1)
SVMNumber = int(3000*1*0.8*0.8)
SVMNumber = int(3000*3*0.3*0.3)
NLPFreqLimit.append(1)
NLPFreqLimit.append(1)
degrees.append(2)
degrees.append(6)
SVMMode = 'ratio'
SVMMode = 'number'
mode = ["max ent"]

outFile = open(fileName,'w')
if degrees == []:
	print "No degrees found, quitting"
	outFile.write('0')
	outFile.close()
	quit()

if ["decision tree"] == mode:
	NLPFreqLimit = [max(2,entry) for entry in NLPFreqLimit]
	degrees = list(set(degrees))[:2]

cfg = {'SVMMode':SVMMode,
	'SVMNumber':SVMNumber,
	'NLPFreqLimit':NLPFreqLimit}

args = {'cores':cores,
	'iterations':iterations,
	'sweepRange':sweepRange,
	'degrees':[list(set(degrees))],
	'mode':mode,
	'cfg':cfg,
	'stops':stops,
	'prefix':prefix,
	'files':files}

try:
	score = int(optimizeClassifier.main(args,'mendel'))
	outFile.write(str(score))
except:
	outFile.write('0')

outFile.close()




