import sys
from collections import defaultdict

words = defaultdict(int)
tags = defaultdict(int)
total_errors = 0

def print_vals():
    global total_errors
    print 'TOTAL NUMBER OF ERRORS:'
    print '---------------------- '
    print '{}'.format(total_errors)
    print
    print
    print 'INCORRECT LABELS: number of incorrect labelings by the data for each correct label'
    print '---------------- '
    for key,value in sorted(tags.iteritems(), key = lambda (k,v): (-v,k)):
        print '{}: {}'.format(key, value)
    print
    print
    print 'INCORRECT WORDS: number of incorrect labelings for a given word'
    print '--------------- '
    for key,value in sorted(words.iteritems(), key = lambda (k,v): (-v,k)):
        print '{}: {}'.format(key, value)

def compare():
    global total_errors
    data = open(sys.argv[1], 'r')
    key = open(sys.argv[2], 'r')
    line_data = data.readline()
    line_key = key.readline()
    while line_data:
        l_d = line_data.strip()
        l_k = line_key.strip()
        if l_d:
            vals_data = l_d.split(' ')
            vals_key = l_k.split(' ')
            if not vals_data[1] == vals_key[1]:
                total_errors += 1
                words[vals_data[0]] += 1
                tags[vals_key[1]] += 1
        line_data = data.readline()
        line_key = key.readline()
    print_vals()

compare()
