import csv
import sys
import math
vector_size = 500
word_vector = {}
topic_vector = []

def vector_add(v1, v2):
    """
    add vector v2 to v1
    """
    if len(v1) != len(v2):
        raise Exception('vector length not match')
    for i in range(len(v1)):
        v1[i] += v2[i]

def load_topic(topic_file):
    with open(topic_file) as csvfile:
        rows = csv.reader(csvfile, delimiter='\t')
        for row in rows:
            topic_name = row[0]
            v = [0.0] * vector_size
            for w in row[1:]:
                if w not in word_vector:
                    continue
                v_w = word_vector[w]
                vector_add(v, v_w)
            topic_vector.append((topic_name, v))
                
def load_word_vector(vector_file):
    with open (vector_file) as csvfile:
        rows = csv.reader(csvfile, delimiter='\t')
        for row in rows:
            v = [float(a) for a in row[1:]]
            word_vector[row[0]] = v

def distance(v1, v2):
    product = 0
    n1 = 0
    n2 = 0
    for (a, b) in zip(v1, v2):
        product += a * b
        n1 += a * a
        n2 += b * b
    if n1 * n2 == 0:
        return float('inf')
    return product / math.sqrt(n1) / math.sqrt(n2)

def find_topic(vector):
    answer = "NOT_FOUND"
    dis = float('-inf')
    for (top_name, top_vec) in topic_vector:
        d = distance(top_vec, vector)
        if d > dis:
            dis = d
            answer = top_name
    return answer

    
def process_maintext(maintext_file, result_file):
    result = open (result_file, "w")
    result_writer = csv.writer(result, delimiter='\t')
    with open(maintext_file) as csvfile:
        articles = csv.reader(csvfile, delimiter='\t')
        for row in articles:
            maintext = row[2]
            #maintext = row[1]
            word_set = maintext.split(' ')
            average = [0.0] * vector_size
            for word in word_set:
                if word not in word_vector:
                    continue
                v_word = word_vector[word]
                vector_add(average, v_word)

            result_writer.writerow([row[1], find_topic(average)])
            print(row[1])
    result.close()

def main():
    vector_file = sys.argv[1]
    topic_file = sys.argv[2]
    maintext_file = sys.argv[3]
    result_file = sys.argv[4]
    load_word_vector(vector_file)
    load_topic(topic_file)
    process_maintext(maintext_file, result_file)

if __name__ == "__main__":
    main()
