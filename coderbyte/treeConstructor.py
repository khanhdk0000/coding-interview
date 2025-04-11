def TreeConstructor(strArr)-> bool: 
    def parse(s):
        a, b = s.strip("()").split(",")
        return int(a), int(b)
    
    parentsOf = {}
    childrenOF = {}
    nodes = set()
    for s in strArr:
        a, b = parse(s)
        nodes.add(a)
        nodes.add(b)
        # Each child can only have one parent
        if a in parentsOf:
            return False
        parentsOf[a] = b

        # Each parent can only at most have two children
        if b in childrenOF:
            childrenOF[b] += 1
            if childrenOF[b] > 2:
                return False
        else:
            childrenOF[b] = 1

    # Check if the tree is valid
    root = None
    for node in nodes:
        if node not in parentsOf:
            if root is not None:
                return False
            root = node
    
    # acyclic check + connected check
    if len(strArr) != len(nodes) - 1:
        return False

    return True

input = ["(1,2)", "(2,4)", "(5,7)", "(7,2)", "(9,5)"] # True
print(TreeConstructor(input))
print(TreeConstructor(["(1,2)", "(3,2)", "(2,12)", "(5,2)"])) # False