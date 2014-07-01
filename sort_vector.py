import math
import sys
def two_norm(v):
    s = 0
    for a in v[1:]:
        s += float(a) * float(a) 
    return (math.sqrt(s), v[0].strip())

vectors = []
for row in sys.stdin:
    vectors.append(two_norm(row.split('\t')))
vectors.sort(reverse=True)
for n,w in vectors:
    print str(n) + '\t' + w
