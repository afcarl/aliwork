import csv
import sys
from collections import Counter
word_topic = {}
def load_topic(topic_file):
    with open(topic_file) as csvfile:
        topics = csv.reader(csvfile)
        for row in topics:
            topic = row[0]
            words = row[1]
            for word in words.split(' '):
                word_topic[word] = topic


def process_maintext(maintext_file, result_file):
    result = open (result_file, "w")
    result_writer = csv.writer(result)
    with open(maintext_file) as csvfile:
        articles = csv.reader(csvfile)
        for row in articles:
            maintext = row[2]
            #word_set = set(maintext.split(' '))
            word_set = maintext.split(' ')
            topic_counter = Counter()
            for word in word_set:
                if word not in word_topic:
                    continue
                topic_counter[word_topic[word]] += 1
            top_topic = topic_counter.most_common(5)
            result_writer.writerow([row[1]] + top_topic)
    result.close()

def main():
    topic_file = sys.argv[1]
    maintext_file = sys.argv[2]
    result_file = sys.argv[3]
    load_topic(topic_file)
    process_maintext(maintext_file, result_file)

if __name__ == "__main__":
    main()
