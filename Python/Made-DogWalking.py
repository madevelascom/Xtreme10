__author__ = 'madevelasco'
import fileinput

def main():
    first = True
    second = True
    third = True
    groups = 0
    walkers = 0
    dog = 0
    dogs = []
    result = []
    i = 0

    for line in fileinput.input():
        if (first):
            groups = int (line)
            first = False
        elif(second):
            line = str(line)
            res = line.strip
            walkers = res[0]
            dog = res [1]
            second = False
        elif(third):
            i += 1
            inp = int(line)
            dogs.append(inp)
            if (i == dog ):
                result.append(sol(walkers, dog, dogs))
                third = False
                i = 0

    for i in result:
        print(i)

def sol(walkers, dog, dogs):
    result = 0
    dogs.sort()
    range = dogs[dog-1] - dogs[0]
    s = []
    m = []
    l = []
    xl = []
    for z in dogs:
       if (z < (dogs[0]+range*0.25)):
           s.append(z)
       elif(z < (dogs[0]+range*0.5)):
           m.append(z)
       elif (z < (dogs[0] + range * 0.75)):
           l.append(z)
       else:
           xl.append(z)





    return result

def merge


if __name__ == '__main__':
    main()