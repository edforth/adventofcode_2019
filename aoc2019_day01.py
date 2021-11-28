with open('day01input.txt',"r") as f:
    lines = f.read().splitlines()

import math

#Part 1
fuelneeded = 0
for line in lines:
    fuelneeded = fuelneeded + (int(line)//3 - 2)
print("Part 1 Answer = ",fuelneeded)
#Correct, first try (3481005)



"""
#Part 2 Take 1
additionalfuelneeded = (fuelneeded//3 -2)
while (additionalfuelneeded//3-2) > 0:
    fuelneeded = fuelneeded + (additionalfuelneeded//3-2)
    additionalfuelneeded = (additionalfuelneeded//3-2)
print("Part 2 Answer = ",fuelneeded)
#4061131 Incorrect (too low)
"""

"""
#Part 2 Take 2
fuelneededformodules = 0
for line in lines:
    fuelneededformodules = fuelneededformodules + (int(line)//3 - 2)
fueltofuel = fuelneededformodules
fuelneededforfuel = 0 
while (fueltofuel//3 - 2) > 0:
    fuelneededforfuel = fuelneededforfuel + (fueltofuel//3 - 2)
    fueltofuel = (fueltofuel//3 - 2)
print("fuelneededformodules",fuelneededformodules)
print("Part 2 Answer =",fuelneededforfuel+fuelneededformodules)
#5221464 Incorrect (Too High)
#Re-reading the puzzle, I'm supposed to calculate each module + fuel seperately
"""

#Part 2 Take 3
fuelneeded = 0
for line in lines:
    fuelneededformodule = (int(line)//3 - 2)
    fueltofuel = fuelneededformodule
    fuelneededforfuel = 0
    while (fueltofuel//3 - 2) > 0:
        fuelneededforfuel = fuelneededforfuel + (fueltofuel//3 - 2)
        fueltofuel = (fueltofuel//3 - 2)
    fuelneeded = fuelneeded + fuelneededformodule + fuelneededforfuel
print("Part 2 Answer =",fuelneeded)
#Correct this time! (5218616)