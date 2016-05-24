import os
import sys

def write_the_thing(pattern, replace, read, write):
    try:
        fin = open(read, 'r')
        try:
            fout = open(write, 'w')
            for line in fin:
                line = line.replace(pattern, replace)
                fout.write(line)
        except:
            print "Could not open " + str(write) + " for Writing"

    except:
        print "Could not open " + str(read) + " for Reading"


def run(pgrm, filenm, pattern='pattern', replace='replacen', write=''):
    read = filenm
    if write == '':
        write = read + '.rename'

    write_the_thing(pattern,replace,read,write)

if __name__ == '__main__':
    print sys.argv
    run(*sys.argv)