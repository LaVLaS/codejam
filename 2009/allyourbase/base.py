#!/usr/bin/python

def scanString(cipherStr, caseNum=-1):
	cipherDict = dict()
	cipherDictIndex = 1
	
	
	for s in cipherStr:
		if s not in cipherDict:
			cipherDict[s] = cipherDictIndex
			if cipherDictIndex == 1:
				cipherDictIndex = 0
			elif cipherDictIndex == 0:
				cipherDictIndex = 2
			else:
				cipherDictIndex += 1

	base = max(len(cipherDict),2)
	
	cipherTotal = 0
	for s in cipherStr:
		cipherTotal = (cipherTotal * base)
		cipherTotal += cipherDict[s]
	
	print "Case #{}: {}".format(caseNum, cipherTotal)


maxTests = int(raw_input())

#print "Total test cases: {}".format(maxTests)

for x in range(1,maxTests+1):
	case = raw_input()
	scanString(case, x)
