# Class BasicSystem:
# This class represents the basic system, contains activators and inhibitors, and the system target (result - active or inactive)

class BasicSystem:
    IN = 2  # Maximum value for n, inhibitors
    AC = 2  # Maximum value for m, activators

    def __init__(self, n_1, m_1, target=False):
        self.n_1 = n_1  # Number of inhibitors for the specific instance
        self.m_1 = m_1  # Number of activators for the specific instance
        self.target = target

    def __repr__(self):
        return f"(n={self.n_1}, m={self.m_1}, target={self.target})"
    
    # Checks if this BasicSystem instance is equal to another instance (for making this class compatible with set data structure):
    def __eq__(self, other):
        if isinstance(other, BasicSystem):
            return (self.n_1 == other.n_1 and
                    self.m_1 == other.m_1 and
                    self.target == other.target)
        return False

    # Computes a hash value for this BasicSystem instance (for making this class compatible with set data structure):
    def __hash__(self):
        return hash((self.n_1, self.m_1, self.target))

    
    # Generate the basic regulation conditions which correspond to the necessary conditions of 
    # monotonic regulation conditions for each of the basic systems:
    def generateAllNecessaryBasicMonotonicRegulationConditions(self):
        conditions = []
        
        # The case of (n_1 = IN, m_2 = 0, target = 1) is forbidden since it will break the assumption
        # that we have mentioned in the main.py program:
        if (self.n_1 == BasicSystem.IN and self.m_1 == 0):
            return conditions # Empty array

        # Ensure we first have the initial system's target in active state 
        self.target = True

        # Iterate over all possible (n_2, m_2) pairs
        for n_2 in range(self.IN + 1):
            for m_2 in range(self.AC + 1):
                # Assume target is False unless proven otherwise
                target = False
                
                # Check conditions based on the provided rules
                if (n_2 == self.n_1 and m_2 >= self.m_1) or (n_2 < self.n_1 and m_2 >= self.m_1):
                    target = True
                
                # Append the condition (n_2, m_2, target) to the conditions list
                conditions.append(BasicSystem(n_2, m_2, target))
        
        return conditions


