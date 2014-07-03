from sys import path
from os import getcwd
parent = '/'.join(getcwd().split('/')[:])
print parent
#parent = '..'
if parent not in path:
	path.insert(0, parent)
import optimizeClassifier

files = ['vaccAutNLPScores.csv']
cores = 2
iterations = 3
sweepRange = [0.9]
degrees =  []
SVMMode = 'number'
SVMNumber = 1000
stops = 0
fileName = "ShakespeareShuffleVacc/ShakespeareShuffleVacc1Score.txt"
index = 1
gen = 0
prefix = ''
mode = ["decision tree"]
SVMNumber = int(3000*7*0.7*0.7)
degrees.append(3)
None
degrees.append(6)
degrees.append(7)
None
degrees.append(7)
SVMMode = 'ratio'
SVMMode = 'all'
SVMNumber = int(3000*5*0.4*0.4)
None
SVMMode = 'all'
degrees.append(7)
SVMMode = 'number'
mode = ["decision tree"]
SVMMode = 'ratio'
degrees.append(7)
None
None

outFile = open(fileName,'w')
cfg = {'SVMMode':SVMMode,
	'SVMNumber':SVMNumber}
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
