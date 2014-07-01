import sys
from collections import Counter

word_cnt = Counter
for line in sys.stdin:
    row = line.split('\t')
    # row[0] is the class id
    for word in row[1:]:
        word_cnt[word.strip()] += 1

for w_c in word_cnt.most_common():
    print w_c[0] + '\t' + w_c[1]

