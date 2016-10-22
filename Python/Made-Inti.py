__author__ = 'madevelasco'

import fileinput
import itertools


def gGDCcd(x,y):
    while y != 0:
        (x, y) = (y, x % y)
    if (x == 1):
        return True
    else:
        return False 

def sum(alist):
    x= 0
    for i in alist:
        x = x + int(i)
    return x

def main():
    first = True
    quan = 0
    aset = []


    for line in fileinput.input():
        if (first):
            quan = int(line)
            first = False
        else:
            max = 0
            line = str(line)
            res = line.strip
            res = line.split(' ')
            res = [int(i) for i in res]
            for L in range(1, len(res)+1):
                for subset in itertools.combinations(res, L):
                    a = reduce(gGDCcd, subset)
                    print (subset, a, 'asdas', sum(subset))
                    if (a):
                        b = sum(subset)
                        if(b > max):
                            max = b


            if (max > res[len(res)-1]):      
                print (max)
            else:
                print(res[len(res)-1])

if __name__ == '__main__':
    main()