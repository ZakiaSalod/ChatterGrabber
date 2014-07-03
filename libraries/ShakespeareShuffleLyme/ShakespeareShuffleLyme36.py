from sys import path
from os import getcwd

parent = '/'.join(getcwd().split('/')[:])

if parent not in path:
	path.insert(0, parent)
import optimizeClassifier

files = ['lymeScores.csv']
cores = 1
iterations = 1
sweepRange = [0.9]
degrees =  []
SVMMode = 'number'
SVMNumber = 1000
NLPFreqLimit = []
stops = 0
prefix = ''



fileName = "ShakespeareShuffleLyme/ShakespeareShuffleLyme36Score.txt"
index = 36
gen = 0

SVMMode = 'number'
SVMNumber = int(3000*1*0.6*0.6)
mode = ["naive bayes"]
SVMMode = 'number'
NLPFreqLimit.append(4)
SVMNumber = int(3000*7*0.7*0.7)
SVMNumber = int(3000*4*0.7*0.7)
degrees.append(2)
NLPFreqLimit.append(1)
NLPFreqLimit.append(3)
SVMNumber = int(3000*7*0.99*0.99)
SVMMode = 'number'
SVMMode = 'number'
SVMMode = 'ratio'
mode = ["naive bayes"]
mode = ["naive bayes"]
mode = ["svm"]
SVMNumber = int(3000*7*0.5*0.5)
mode = ["decision tree"]
NLPFreqLimit.append(3)

outFile = open(fileName,'w')
if degrees == []:
	print "No degrees found, quitting"
	outFile.write('0')
	outFile.close()
	quit()

if mode == "decision tree":
	NLPFreqLimit = [max(2,entry) for entry in NLPFreqLimit]
	degrees = list(set(degrees))[:1]

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



