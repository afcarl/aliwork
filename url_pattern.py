from collections import Counter
import sys
class Tree():
    def __init__(self, name):
        self.name = name
        self.count = 0
        self.child = {}
    def add(self, path):
        self.count += 1
        if len(path) == 0:
            return
        ch = path[0]
        if ch not in self.child:
            self.child[ch] = Tree(ch)
        self.child[ch].add(path[1:])

def output_tree(tree, prefix = None):
    if prefix:
        path = prefix + '.' + tree.name
    else:
        path = tree.name
    print path + '\t' + str(tree.count)
    for child in tree.child.itervalues():
        output_tree(child, path)

def parse_url(url):
    s_url = url.split('://')
    address = s_url[1]
    s_address = address.split('/')
    host = s_address[0]
    path = s_address[1:]
    s_host = host.split('.')
    elements = s_host[::-1]
    if len(path) >= 2:
        if len(path) >= 2:
            elements.append('/' + path[0])
        if len(path) >= 3:
            elements.append('/' + path[1])
    return elements


pattern_counter = Counter()
root = Tree("http://")
def process_file():
    for linenum, line in enumerate(sys.stdin):
        if linenum % 1000000 == 0:
            sys.stderr.write(str(linenum) + '\n')
        s_line = line.split(',')
        url = s_line[0]
        #add_to_tree(parse_url(url))
        root.add(parse_url(url))
        #pattern_counter['.'.join(parse_url(url))] += 1

def output():
    #for pat, cnt in pattern_counter.most_common():
    #    print pat, cnt
    output_tree(root)

def main():
    process_file()
    output()
if __name__ == '__main__':
    main()
