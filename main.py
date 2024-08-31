#######################
# Ziv Chaba 326681285 #
# Bar Zomer 326400454 #
#######################

'''
First, we will create the most basic monotonic regulation conditions (or, functions).

Each basic regulation condition correspond to the necessary conditions of 
monotonic regulation conditions - Given IN, the number of inhibitors, 
and AC, the number of activators in the system, if for a pair (# inhibitors, # activators) = (n_1, m_1),
their target is 1, then for every [n_2 = n_1] [m_1 < m_2 <= AC] the pairs (n_2, m_2) have target = 1,
and also for every [n_2 < n_1] & [m_2 >= m_1] the pairs (n_1, m_2) have target = 1.
We have the assumption that, for each regulation condition, the component cannot be constantly 
activated or repressed regardless of the state of each regulators, and therefore
states (n = IN, m = 0, target = 1), (n = 0, m = AC, target = 0) are forbidden.


After that, with those basic monotonic regulation conditions,
we can expand and complete our set of monotonic regulation conditions by 
committing monotonicity-preserving operations for boolean functions - AND , OR,
between the basic monotonic regulation conditions (functions) that we have already found.
'''

from BasicSystem import BasicSystem

# Function that generates all possible BasicsSystem objects:
def generateAllBasicSystems(IN, AC):
    systems = []
    for n in range(IN + 1):
        for m in range(AC + 1):
            systems.append(BasicSystem(n, m))
    return systems

# Function to perform logical AND between target fields of two tuples
def logicalAnd(t1, t2):
    return tuple(BasicSystem(t1[i].n_1, t1[i].m_1, t1[i].target and t2[i].target) for i in range(len(t1)))

# Function to perform logical OR between target fields of two tuples
def logicalOr(t1, t2):  
    return tuple(BasicSystem(t1[i].n_1, t1[i].m_1, t1[i].target or t2[i].target) for i in range(len(t1)))





def main():
    allBasicSystems = generateAllBasicSystems(BasicSystem.IN, BasicSystem.AC)
    
    # All the necessary (prior) monotonic regulation conditions (functions) set:
    allNecessaryMonotonicRegulationConditions = set()
    for system in allBasicSystems:
        allNecessaryMonotonicRegulationConditions.add(tuple(system.generateAllNecessaryBasicMonotonicRegulationConditions()))
        '''
        # This section may be uncommented for a better view of all the necessary (prior) monotonic regulation conditions (functions) 
        # Print all the prior sets:

        print("The necessary (prior) monotonic regulation condition for", system, "is: ")
        print(tuple(system.generateAllNecessaryBasicMonotonicRegulationConditions()))
        print("------------------------------------", end = "\n\n")
        '''

    # Remove the empty tuple due to the forbidden state:
    allNecessaryMonotonicRegulationConditions = [t for t in allNecessaryMonotonicRegulationConditions if t]
    allNecessaryMonotonicRegulationConditions = list(allNecessaryMonotonicRegulationConditions)

    
    # Complete the set of monotonic regulation conditions by committing 
    # monotonicity-preserving operations for boolean functions - AND , OR.
    # Do it until there are no changes.

    # All monotonic regulation conditions (functions) set:
    allMonotonicRegulationConditions = set(allNecessaryMonotonicRegulationConditions)
    allMonotonicRegulationConditionsOld = list(allMonotonicRegulationConditions)  # the allMonotonicRegulationConditions last iteration
    wasChange = 1

    while(wasChange):
        # Iterate over each pair of tuples in the set
        for i in range(len(allMonotonicRegulationConditionsOld)):
            for j in range(i, len(allMonotonicRegulationConditionsOld)):
                t1 = allMonotonicRegulationConditionsOld[i]
                t2 = allMonotonicRegulationConditionsOld[j]
                
                # Perform AND operation
                andResult = logicalAnd(t1, t2)
                allMonotonicRegulationConditions.add(andResult)
                
                # Perform OR operation
                orResult = logicalOr(t1, t2)
                allMonotonicRegulationConditions.add(orResult)
        
        # Check for change from last iteration:
        if (list(allMonotonicRegulationConditions) == list(allMonotonicRegulationConditionsOld)):
            wasChange = 0
        else:
            allMonotonicRegulationConditionsOld = list(allMonotonicRegulationConditions)

    
    print(f"There are {len(allMonotonicRegulationConditions)} monotonic regulation conditions.\n")
    print(f"All {len(allMonotonicRegulationConditions)} monotonic regulation conditions are: \n")
    count=0
    for i in allMonotonicRegulationConditions:
        print(count, end=". ")
        print(i, end="\n\n\n")
        count+=1


if __name__ == "__main__":
    main()
