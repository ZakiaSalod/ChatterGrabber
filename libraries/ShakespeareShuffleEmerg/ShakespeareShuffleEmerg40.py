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



fileName = "ShakespeareShuffleEmerg/ShakespeareShuffleEmerg40Score.txt"
index = 40
gen = 0

mode = ["decision tree"]
mode = ["max ent"]
NLPFreqLimit.append(4)
SVMNumber = int(3000*3*0.8*0.8)
SVMMode = 'number'
SVMNumber = int(3000*4*0.1*0.1)
SVMNumber = int(3000*4*0.5*0.5)
SVMNumber = int(3000*1*0.2*0.2)
degrees.append(2)
NLPFreqLimit.append(2)
NLPFreqLimit.append(3)
SVMMode = 'ratio'
degrees.append(1)
SVMNumber = int(3000*5*0.5*0.5)
mode = ["svm"]
degrees.append(6)
mode = ["decision tree"]
SVMMode = 'number'
mode = ["decision tree"]
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



