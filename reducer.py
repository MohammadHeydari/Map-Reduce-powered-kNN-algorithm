#!/usr/bin/env python
import sys
from operator import itemgetter
distances=[]
estimateval = 0.0
k=3
#k=int(sys.argv[1])

for lines in sys.stdin:
	lines=lines.strip()
	elements = lines.split(',')
	distances.append(elements)
distances = sorted(distances,key=itemgetter(-1))

for i in range(k):
	try:
		estimateval += float(distances[i][-2])
	except ValueError:
		continue
	
print estimateval/k

