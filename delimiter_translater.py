import csv
import sys
def translate(input, deli_in, output):
    """
    translate a csv file with delimiter deli_in into
    that with delimiter '\t'
    """
    output_file = open(output, 'w')
    writer = csv.writer(output_file, delimiter='\t')
    with open(input) as input_file:
        reader = csv.reader(input_file, delimiter=deli_in)
        for row in reader:
            newrow = [item.replace('\t', ' ') for item in row]
            writer.writerow(newrow)
    output_file.close()

if __name__ == '__main__':
    input = sys.argv[1]
    deli_in = sys.argv[2]
    print(deli_in)
    output = sys.argv[3]
    translate(input, deli_in, output)

