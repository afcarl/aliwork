import sys
def rebuild(url_pat):
    s_url_pat = url_pat.split("./")
    host = s_url_pat[0]
    path = s_url_pat[1:]
    s_host = host.split('.')
    host = 'http://' + '.'.join(reversed(s_host[1:]))
    return '/'.join([host] + path)
def main():
    for line in sys.stdin:
        row = line.split('\t')
        url = rebuild(row[0])
        print url + '\t' + row[1].strip() + '\t' + url
if __name__ == '__main__':
    main()
