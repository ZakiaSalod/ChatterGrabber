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



fileName = "ShakespeareShuffleLyme/ShakespeareShuffleLyme31Score.txt"
index = 31
gen = 0

SVMMode = 'ratio'
mode = ["max ent"]
mode = ["naive bayes"]
degrees.append(7)
degrees.append(1)
NLPFreqLimit.append(3)
SVMMode = 'ratio'
NLPFreqLimit.append(4)
NLPFreqLimit.append(2)
mode = ["max ent"]
mode = ["max ent"]
NLPFreqLimit.append(1)
SVMNumber = int(3000*6*0.8*0.8)
SVMMode = 'all'
SVMNumber = int(3000*6*0.7*0.7)
NLPFreqLimit.append(2)
degrees.append(6)
SVMNumber = int(3000*2*0.1*0.1)
mode = ["decision tree"]
SVMNumber = int(3000*2*0.7*0.7)

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



