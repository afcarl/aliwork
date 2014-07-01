import sys
stop_words = dict() 
stop_words_set = set()
stop_word_file = open('/home/pawnty.ty/data/stop_words')
lenline = 0
for line in stop_word_file:
    stop_words_set.add(line.strip())

for line_number, line in enumerate(sys.stdin):
    lenline = line_number
    row = line.split('\t')
    n, w = row[0], row[1].strip()
    if w in stop_words_set:
        stop_words[w] = (line_number, n)

for w, s in stop_words.items():
    print str(float(s[0]) / lenline) + '\t' + str(s[1]) + '\t' + w

