from calculator import calculator
def calcul_orchestrator(elements):
    """
    calcul_orchestrator(tuple) -> float
    A recursive function that process any simple operation
    passed as parameter and return a float as result. It 
    handles infinite parenthesis recursion and classic 
    operators priority.
    """
    # elements_levels init
    elements_levels = []
    for i in range(len(elements)): 
        elements_levels.append((elements[i],0))
    
    # parenthesis init
    parenthesis = False 
    # check if there is a parenthesis in the elements
    for i in range(len(elements)):
        if elements[i] == "(":
            parenthesis = True
            break
    """ 
    while we find parenthesis in elements_levels we put 
    what's between parenthesis in sub_calculation list 
    and replace what's between parenthesis with 
    calcul_orchestrator(sub_calculation) output 
    """
    while parenthesis:
        level = 0
        sub_calculation = []
        for i in range(len(elements_levels)):
            if elements_levels[i][0] == "(":
                opener_index = i
                break
        # Scan elements: increasing level when "(" found and decreasing when ")" found
        for i in range(len(elements_levels)):
            if elements_levels[i][0] == "(":
                level += 1
            elif elements_levels[i][0] == ")":
                level -= 1
            # Assign level to every element
            elements_levels[i] = (elements_levels[i][0],level)
        for i in range(len(elements_levels)):
            if i > opener_index and elements_levels[i][1] < 1:
                closer_index = i
                break
        # opener_index +1 to skip the opening parenthesis
        for i in range(opener_index+1,closer_index): 
            sub_calculation.append(elements_levels[i][0])

        # Remove sub_calculation elements from elements_levels
        for i in range(closer_index,opener_index,-1):
            elements_levels.pop(i) 
        
        # Replace opener_index value with sub_calculation result (recursive call)
        elements_levels[opener_index] = (calcul_orchestrator(tuple(sub_calculation)),0) 
        
        # Parenthesis presence check
        for i in range(len(elements_levels)):
            if elements_levels[i][0] == "(":
                parenthesis = True
                break
            else:
                parenthesis = False

#######################################################################################
    # Orchestring operations when no parenthesis is found
    elements_levels_remaining = True
    i = 0
    # First loop for multiplication and divisions
    while elements_levels_remaining:
        if elements_levels[i][0] == "*" or elements_levels[i][0] == "/":
            elements_levels[i-1] = (calculator(elements_levels[i-1][0],elements_levels[i+1][0],elements_levels[i][0]),0)
            elements_levels.pop(i+1)
            elements_levels.pop(i)
            i-=1
        else:
            i+=1
            if len(elements_levels) <= i:
                elements_levels_remaining = False
    elements_levels_remaining = True
    i = 0
    # Second loop for additions and substractions
    while elements_levels_remaining:
        if elements_levels[i][0] == "+" or elements_levels[i][0] == "-":
            elements_levels[i-1] = (calculator(elements_levels[i-1][0],elements_levels[i+1][0],elements_levels[i][0]),0)
            elements_levels.pop(i+1)
            elements_levels.pop(i)
            i-=1
        else:
            i+=1
            if len(elements_levels) <= i:
                elements_levels_remaining = False
    return elements_levels[0][0] # Return what's left at the end