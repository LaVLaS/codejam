#!/usr/bin/python

debugOutput = False

maxTestCases = int(raw_input().strip())
if debugOutput:
	print maxTestCases

for testCase in xrange(1, maxTestCases+1):
	vectorLength = int(raw_input().strip())
	vec1 = [int(x) for x in raw_input().strip().split(' ')]
	vec2 = [int(x) for x in raw_input().strip().split(' ')]
	
	if debugOutput:
		print vectorLength
		print ' '.join(map(str,vec1)) 
		print ' '.join(map(str,vec2)) 

	vec1.sort()
	vec2.sort(reverse=True)
	
	scalProd = 0
	for x in range(0,vectorLength):
		scalProd += vec1[x] * vec2[x]

	print "Case #{}: {}".format(testCase, scalProd)

