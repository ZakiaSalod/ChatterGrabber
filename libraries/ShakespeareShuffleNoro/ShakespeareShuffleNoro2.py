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



fileName = "ShakespeareShuffleNoro/ShakespeareShuffleNoro2Score.txt"
index = 2
gen = 36

degrees.append(4)
mode = ["max ent"]
mode = ["naive bayes"]
mode = ["max ent"]
SVMNumber = int(3000*5*0.7*0.7)
mode = ["svm"]
mode = ["svm"]
mode = ["decision tree"]
mode = ["naive bayes"]
degrees.append(1)
NLPFreqLimit.append(3)
degrees.append(2)
SVMMode = 'ratio'
SVMNumber = int(3000*1*0.2*0.2)
mode = ["decision tree"]
SVMNumber = int(3000*4*0.1*0.1)
SVMNumber = int(3000*5*0.6*0.6)
degrees.append(1)
mode = ["svm"]
degrees.append(7)

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



