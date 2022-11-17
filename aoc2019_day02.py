from pprint import pprint
from inspect import getmembers

def part2(filename):
    answer = ''
    with open(filename,"r") as f:
        lines = f.read().strip().split(",")
    
    return answer

def part1(filename):
    answer = ''
    with open(filename,"r") as f:
        lines = f.read().strip().split(",")
    #print(lines)
    currentpos = 0 
    lines[1] = 12
    lines[2] = 2
    while currentpos <= (len(lines) -1):
        loopvalue = int(lines[currentpos])
        factor1pos = int(lines[currentpos+1])
        factor1value = int(lines[factor1pos])
        factor2pos = int(lines[currentpos+2])
        factor2value = int(lines[factor2pos])
        position = int(lines[currentpos+3])
        #print('loopvalue = ' + str(loopvalue))
        #pprint(loopvalue)
        #print('beginning of loop currentpos = ' + str(currentpos))      
        #print('beginning of loop value of lines[currentpos] = ' + lines[currentpos])      
        #print(lines[currentpos])
        if loopvalue == 1:
            #print('==1')
            lines[position] = factor1value + factor2value
            #print('position #' + str(position) + ' changed to ' + str(factor1value + factor2value))
            #print('lines['+ str(position) + '] = ' + str(lines[position]))
        elif loopvalue == 2: 
            #print('==2')
            lines[position] = factor1value * factor2value
            #print('position #' + str(position) + ' changed to ' + str(factor1value * factor2value))
            #print('lines['+ str(position) + '] = ' + str(lines[position]))
        elif loopvalue == 99:
            #print('==99')
            #print('about to break!')
            break
            print('already broke!')
        else:
            #print('==summthingelse')
            #print("error!")
            break
        currentpos = currentpos + 4 
        #print('end of loop currentpos = ' + str(currentpos))
    answer = lines[0]
    return answer


#print("Part 1 Answer = " + str(part1('day02input.txt'))) 
#First attempt 148 - too low
#Second attempt correct with 5866663.   It turns out I was reading the entries after the ops code as the factor values, 
# not as the positions of the factor values
print("Part 2 Answer = " + str(part2('day02input.txt'))) 

