"""
remove the white space at the begining and end of a line
"""
import sys
for line in sys.stdin:
    sys.stdout.write(line.strip() + '\n')
