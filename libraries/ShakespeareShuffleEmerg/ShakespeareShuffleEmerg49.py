from sys import path
from os import getcwd

parent = '/'.join(getcwd().split('/')[:])

if parent not in path:
	path.insert(0, parent)
import optimizeClassifier

files = ['EmergNLTKScoring.csv']
cores = 1
iterations = 1
sweepRange = [0.9]
degrees =  []
SVMMode = 'number'
SVMNumber = 1000
NLPFreqLimit = []
stops = 0
prefix = ''



fileName = "ShakespeareShuffleEmerg/ShakespeareShuffleEmerg49Score.txt"
index = 49
gen = 0

NLPFreqLimit.append(2)
NLPFreqLimit.append(3)
degrees.append(6)
SVMNumber = int(3000*7*0.99*0.99)
SVMNumber = int(3000*1*0.99*0.99)
NLPFreqLimit.append(4)
mode = ["naive bayes"]
NLPFreqLimit.append(3)
NLPFreqLimit.append(4)
mode = ["max ent"]
SVMNumber = int(3000*7*0.99*0.99)
degrees.append(5)
degrees.append(6)
SVMNumber = int(3000*1*0.4*0.4)
mode = ["naive bayes"]
degrees.append(7)
mode = ["svm"]
NLPFreqLimit.append(4)
SVMMode = 'all'
SVMMode = 'number'

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




