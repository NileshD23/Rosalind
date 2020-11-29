def Fibonacci_Loop_Pythonic(months, offspring):
    parent, child = 1, 1
    for itr in range(months - 1):
        child, parent = parent, parent + (child * offspring)
    return child

"""
o - small (children) rabbits. They have to mature and reproduce in the next cycle only
0 - mature(parents) rabbits. They can reproduce and move to the next cycle.

Month 1: [o]
Month 2: [0]
Month 3: [0 o o]
Month 4: [0 o o 0 0]
Month 5: [0 o o 0 0 0 o o 0 o o]
Month 6: [0 o o 0 0 0 o o 0 o o 0 o o 0 0 0 o o 0 0]
"""

def Wascally_Wabbits(month, offspringCount):
    if month == 1:
        return 1
    
    elif month == 2:
        return offspringCount
    
    oneGen = Wascally_Wabbits(month - 1, offspringCount)
    twoGen = Wascally_Wabbits(month - 2, offspringCount)
    
    if month <= 4:
        return (oneGen + twoGen)
    
    return (oneGen + (twoGen * offspringCount))

print(Fibonacci_Loop_Pythonic(35, 5))
print(Wascally_Wabbits(35, 5)) # much slower to compute