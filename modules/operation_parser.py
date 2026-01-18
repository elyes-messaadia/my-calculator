def operation_parser(operation):
    """Convert an operation string into a Tuple list of each elements"""

    try :
        elements = ()
        number = "" # Initialize number to empty string

        for i in range(len(operation)): # for each character in operation string
            match operation[i]:
                case "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9" | ".":
                    number += operation[i] #build the number
                
                case "(" | ")" | "+" | "-" | "/" | "*" | "^" | "%" | "!":
                    if not number=="":   
                        elements += (float(number),) # add the number to elements
                        number="" # Reset the number
                    # Verify if - is operator or negative number
                    if operation[i] == "-":
                        if i == 0:
                            number += operation[i]
                        elif (operation[i-1] == "(" or 
                              operation[i-1] == "*" or 
                              operation[i-1] == "/" or
                              operation[i-1] == "//" or
                              operation[i-1] == "^" or
                              operation[i-1] == "!"):
                            number += operation[i]
                        else:
                            elements += (operation[i],)
                    # Verify if / or //
                    elif operation[i] == "/": 
                        if operation[i+1] == "/":
                            elements += ("//",)
                        elif operation[i-1] == "/": # Avoid adding another double break if there's already one
                            continue
                    else:     
                        elements += (operation[i],) 

        if not number=="":
            elements += (float(number),) # Add this if it finish with a number
        return elements

    except Exception as e:
        return ("Error: operation_parser module error", e)

