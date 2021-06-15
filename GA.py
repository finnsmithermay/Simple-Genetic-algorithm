
import random


#function to optermise
#goal to make this output 25 and the minus 25 is so we can use 0 
def foo(x,y,z):
    return 6*x**3 + 9*y**2 + 90*z - 25


#fitness function giving score from how close to 0
#abs to handle negitive numbers and they have the same fitness
def fitness(x,y,z):
    ans = foo(x,y,z)

    if ans == 0:
        return 99999
    else:
        return abs(1/ans)


#generat solutions
solutions = []
for s in range(1000):
    solutions.append( (random.uniform(0,10000),
                       random.uniform(0,10000),
                       random.uniform(0,10000)) ) 



for i in range(500):
    rankedSolutions = []
    for s in solutions:
        rankedSolutions.append((fitness(s[0],s[1],s[2]),s))
    rankedSolutions.sort()
    rankedSolutions.reverse()

    print(f"=== Gen {i} best solutions === ")


    print(rankedSolutions[0])

    if rankedSolutions[0][0] > 999:
        break

    #combine best solutions
    bestSolutions = rankedSolutions[:100]

    elements = []
    for s in bestSolutions:
        #getting the x,y,z values
        elements.append(s[1][0])
        elements.append(s[1][1])
        elements.append(s[1][2])

    newGen = []
    for _ in range(1000):
        #get random parts of best solutions and mutate
        #mutate by 2%
        e1 = random.choice(elements) * random.uniform(0.99,1.01)
        e2 = random.choice(elements) * random.uniform(0.99,1.01)
        e3 = random.choice(elements) * random.uniform(0.99,1.01)

        newGen.append((e1,e2,e3))

    solutions = newGen





