from calculator import calculator
def calcul_orchestrator(elements):
    """
    calcul_orchestrator(tuple) -> float
    
    """
    elements_levels = []
    for i in range(len(elements)): # elements_levels init
        elements_levels.append((elements[i],0))
    
    parenthesis = False # parenthesis init
    # check if there is a parenthesis in the elements
    for i in range(len(elements)):
        if elements[i] == "(":
            parenthesis = True
            break
    """ while we find parenthesis in elements_levels we put 
    what's between parenthesis in sub_calculation list and replace
    what's between parenthesis with calcul_orchestrator(sub_calculation) output """
    while parenthesis:
        level = 0
        sub_calculation = []
        for i in range(len(elements_levels)):
            if elements_levels[i][0] == "(":
                opener_index = i
                break
        # Scan elements increase level when finding "(" and decrease when finding ")"
        for i in range(len(elements_levels)):
            if elements_levels[i][0] == "(":
                level += 1
            elif elements_levels[i][0] == ")":
                level -= 1
            elements_levels[i] = (elements_levels[i][0],level)
        for i in range(len(elements_levels)):
            if i > opener_index and elements_levels[i][1] < 1:
                closer_index = i
                break
        for i in range(opener_index+1,closer_index): # opener_index +1 to skip the opening parenthesis
            sub_calculation.append(elements_levels[i][0])
        print(f"elements_levels_before_replacement: {elements_levels}")
        for i in range(closer_index,opener_index,-1):
            elements_levels.pop(i) # Remove sub_calculation elements from elements_levels
        
        elements_levels[opener_index] = (calcul_orchestrator(tuple(sub_calculation)),0) # Replace opener_index value because it's "("
        
        """  #print(f"i: {i}")
        print(f"elements_levels: {elements_levels}")
        print(f"opener_index: {opener_index}")
        print(f"closer_index: {closer_index}")
        print(f"sub_calculation: {sub_calculation}") """
        
        # Parenthesis presence check
        for i in range(len(elements_levels)):
            if elements_levels[i][0] == "(":
                parenthesis = True
                break
            else:
                parenthesis = False

    # Orchestring operations when no parenthesis is found
    elements_levels_remaining = True
    i = 0
    while elements_levels_remaining: # First loop for multiplication and divisions
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
    while elements_levels_remaining: # Second loop for additions and substractions
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

# ((3+6*7)*57)        
#my_elements = ("(","(",3,"+",6,"*",7,")","*",57,")")
# 6*8/((3-2)+4)
#my_elements2 = (6,"*",8,"/","(","(",3,"-",2,")","+",4,")")
# (6+8)/(3-2)+4
#my_elements3 = ("(",6,"+",8,")","/","(",3,"-",2,")","+",4)
#print(calcul_orchestrator(my_elements))
#print(calcul_orchestrator(my_elements2))
#print(calcul_orchestrator(my_elements3))